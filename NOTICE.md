# Источники и лицензии

Основа: DarkFlippers/unleashed-firmware, GPL-3.0,
https://github.com/DarkFlippers/unleashed-firmware/tree/9c6327764c18fc8376b5941aa8bde79fe681fe8f

Адаптация визуального решения вертикальных ползунков:
Next-Flip/Momentum-Firmware, GPL-3.0,
commit d3f89dfe2ef6b01839201598e9be1590cba80322,
applications/services/desktop/views/desktop_view_lock_menu.c.
https://github.com/Next-Flip/Momentum-Firmware/blob/d3f89dfe2ef6b01839201598e9be1590cba80322/applications/services/desktop/views/desktop_view_lock_menu.c

Изменения Hybridus — GPL-3.0; исходные уведомления авторов основы сохранены.
Текст GPL находится в LICENSE. Лицензии компонентов сохранены в исходниках.
Официальной сборкой Unleashed или Momentum этот проект не является.

Подтверждение механизма цвета в открытом Android-клиенте:
https://github.com/flipperdevices/Flipper-Android-App/blob/dev/components/bridge/connection/feature/device-color/impl/src/commonMain/kotlin/com/flipperdevices/bridge/connection/feature/devicecolor/impl/api/FDeviceColorFeatureApiImpl.kt
Клиент читает HARDWARE_COLOR, сопоставляет только WHITE/BLACK/TRANSPARENT,
остальные значения заменяет значением default. Проверка относится к просмотренной
ветке; приложение на телефоне владельца ещё не установлено по версии.

https://momentum-fw.dev/wiki/Misc/Spoofing — смысл Shell Color.
https://developer.flipper.net/flipperzero/doxygen/apps_on_sd_card.html — SDK/FAP.

Никаких секретных данных, приватных ключей или учётных данных в архиве нет.

Версия 0.2: firmware-only наложение на уже установленную 095E, без поставки
или замены её ресурсов. Стандартный SDK 88.26 не менялся. Цвет — встроенный
пункт Phone Shell в Settings; исходный Desktop Settings.fap остаётся на SD.
Установщик содержит явно ограниченный preserve-режим для этого пакета.
Не является официальной Unleashed и не проходил аппаратных испытаний.

Версия 0.3: одностраничная панель с прямым управлением ползунками,
системными переключателями Bluetooth/HandOrient, sound-only Mute.
Динамические виртуальные категории в основном меню из существующих /ext/apps.
Старый Apps остаётся. Диагностика HAL-цвета, не исправление Android-клиента.

Версия 0.4: одно меню на категорию с индивидуальными штатными иконками,
виртуальное объединение штатных инструментов/Apps; Phone Shell — только Color.
Сообщение владельца 17.11.2026: цвет и Quick Settings 0.3 работают.
Их backend/панель в 0.4 не менялись, удалены только диагностические UI-строки.

Версия 0.5: названия категорий как в Apps, включая Tools; алфавитный порядок
без учёта регистра. В Tools остаётся Clock, иконка прежняя; дополнительной
категории/копии файлов не создаётся. Остальные функции 0.4 не изменены.
