#!/usr/bin/env python3
"""Only copy/verify an upstream minimal package. Never connect to a device."""
from pathlib import Path,PurePosixPath
import tarfile,gzip,io,zlib,hashlib,struct,json,sys,shutil
root=Path(sys.argv[1]).resolve();suffix='hybridus-ui-0.7-095e-preserve'
p=root/f'dist/f7-C/flipper-z-f7-update-{suffix}.tgz';data=p.read_bytes()
raw=gzip.decompress(data)
with tarfile.open(fileobj=io.BytesIO(raw)) as tf:
 files={}
 for m in tf:
  path=PurePosixPath(m.name)
  assert not path.is_absolute() and '..' not in path.parts and not m.issym() and not m.islnk()
  if m.isfile():assert path.name not in files;files[path.name]=tf.extractfile(m).read()
assert set(files)=={'update.fuf','updater.bin','firmware.dfu'},set(files)
fields={l.split(':',1)[0]:l.split(':',1)[1].strip() for l in files['update.fuf'].decode().splitlines() if ':' in l}
assert fields['Info']==suffix and fields['Target']=='7'
assert fields['Filetype']=='Flipper firmware upgrade configuration'
assert fields['Loader']=='updater.bin' and fields['Firmware']=='firmware.dfu'
for forbidden in ['Radio','Resources','Splashscreen','OB reference','OB mask','OB write mask']:
 assert not fields.get(forbidden,''),forbidden
for zero in ['Radio address','Radio version','Radio CRC']:
 assert not any(bytes.fromhex(fields.get(zero,''))),zero
assert struct.pack('<I',zlib.crc32(files['updater.bin']))==bytes.fromhex(fields['Loader CRC'])
f=files['firmware.dfu'];assert f[:6]==b'DfuSe\x01' and f[-8:-5]==b'UFD' and f[-5]==16
assert struct.unpack_from('<I',f,6)[0]==len(f)-16
assert struct.unpack('<I',f[-4:])[0]==zlib.crc32(f[:-4])^0xffffffff
assert struct.unpack('<HHHH',f[-16:-8])==(0xffff,0xdf11,0x0483,0x011a)
assert f[10]==1 and f[11:17]==b'Target'
size,count=struct.unpack_from('<II',f,277);assert count==1
addr,n=struct.unpack_from('<II',f,285);assert addr==0x08000000 and size==n+8 and len(f)==n+309
# In this release radio is left in place at 0x080d7000.
assert addr+n<0x080d7000
assert ((addr+n+4095)//4096)*4096 <= 0x080d7000
assert len(files['updater.bin']) < 128*1024
objcopy=root/'toolchain/current/bin/arm-none-eabi-objcopy'
import subprocess,tempfile
with tempfile.TemporaryDirectory() as d:
 for prefix,name,expected in [('firmware','full',f[293:-16]),('updater','updater',files['updater.bin'])]:
  elf=root/f'dist/f7-C/flipper-z-f7-{prefix}-{suffix}.elf'
  out=Path(d)/'binary.bin';subprocess.run([str(objcopy),'-O','binary',str(elf),str(out)],check=True)
  assert out.read_bytes()==expected
# Exact public SDK and external settings source retained.
base=subprocess.check_output(['git','show','HEAD:targets/f7/api_symbols.csv'],cwd=root).replace(b'\r\n',b'\n')
assert (root/'targets/f7/api_symbols.csv').read_bytes().replace(b'\r\n',b'\n')==base
for name in ['applications/settings/desktop_settings/scenes/desktop_settings_scene_start.c','applications/settings/desktop_settings/application.fam']:
 assert (root/name).read_bytes()==subprocess.check_output(['git','show','HEAD:'+name],cwd=root)
# Minimal builder itself is unmodified, so no custom tar path or install script invented.
for name in ['SConstruct','scripts/update.py','lib/update_util/update_manifest.c']:
 assert (root/name).read_bytes()==subprocess.check_output(['git','show','HEAD:'+name],cwd=root)
result={'filename':p.name,'size':len(data),'sha256':hashlib.sha256(data).hexdigest(),'files':{n:{'size':len(b),'sha256':hashlib.sha256(b).hexdigest()} for n,b in files.items()},'manifest':files['update.fuf'].decode(),'dfu_end':hex(addr+n),'api':'88.26','build_base':'9c6327764c18fc8376b5941aa8bde79fe681fe8f','install_mode':'upstream updater_minpackage with exact opt-in preserve updater','hardware_tested':False}
outdir=Path(__file__).resolve().parent
shutil.copyfile(p,outdir/p.name);(outdir/'VERIFICATION.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
