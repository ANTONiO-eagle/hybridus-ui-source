# Hybridus UI 0.7 — снимок исходников API 88.26

Версия изменена относительно [Unleashed `unlshd-095`](https://github.com/DarkFlippers/unleashed-firmware/tree/9c6327764c18fc8376b5941aa8bde79fe681fe8f) (`9c6327764c18fc8376b5941aa8bde79fe681fe8f`) опубликованным [GPL-патчем Hybridus UI 0.7](https://github.com/ANTONiO-eagle/hybridus-ui-source/blob/b77b735c54d21a7b802dfbe2b1bc8403c7a4c32e/hybridus-ui-0.7-095e-preserve.patch). Изменения Hybridus от 17.11.2026, снимок от 20.11.2026. Это не официальный релиз Unleashed и не исходники установленной сборки API 88.27 LTO.

- Архив: [hybridus-ui-0.7-full-source-snapshot-095e.tgz](./hybridus-ui-0.7-full-source-snapshot-095e.tgz)
- Размер: 22025208 байт; файлов: 5028.
- SHA-256: `3aeee92ce9f9b70ac8172e427191b744382e189496f5eb90b840c0167b7fa65f`.
- В архиве — дерево исходников и ресурсов основного репозитория, в том числе штатные upstream-тестовые данные, плюс `HYBRIDUS-CHANGES.md`. Производная прошивка VGM Display, её исходники, Desktop Settings VGM FAP, изменения DUCKY_LANG и готовые к прошивке образы не включены.

## Просмотр и сборка

Проверьте `sha256sum hybridus-ui-0.7-full-source-snapshot-095e.tgz`, затем распакуйте архив через `tar -xzf hybridus-ui-0.7-full-source-snapshot-095e.tgz`. Снимок не является Git-клоном и не содержит рабочих деревьев внешних подмодулей. Для чистой сборки используйте [`build.sh`](./build.sh) из клона этого репозитория: он клонирует точную базу, инициализирует подмодули, проверяет и накладывает патч, запускает FBT. Коммиты прямых зависимостей перечислены в [`SUBMODULES-PINNED.txt`](./SUBMODULES-PINNED.txt). Скрипт не прошивает устройство.

Содержимое дерева сверено с базой и опубликованным патчем. Снимок отдельно на устройстве не испытывался. Отдельные [Quick Settings #1225](https://github.com/DarkFlippers/unleashed-firmware/pull/1225) и [навигация #1226](https://github.com/DarkFlippers/unleashed-firmware/pull/1226) направлены в Unleashed, но публикация этого снимка не является их включением в основную ветку.

## Лицензия и авторство

Изменения Hybridus распространяются по [GPL-3.0](./LICENSE); исходные уведомления и лицензии upstream-компонентов сохранены. Адаптация визуального решения вертикальных ползунков — Next-Flip/Momentum-Firmware, GPL-3.0, [коммит `d3f89df`](https://github.com/Next-Flip/Momentum-Firmware/blob/d3f89dfe2ef6b01839201598e9be1590cba80322/applications/services/desktop/views/desktop_view_lock_menu.c); см. также [`NOTICE.md`](./NOTICE.md). Код изменений и сопроводительные материалы подготовлены с помощью ИИ.
