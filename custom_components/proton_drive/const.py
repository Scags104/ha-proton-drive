"""Constants for the Proton Drive integration."""

from logging import Logger, getLogger

LOGGER: Logger = getLogger(__package__)

DOMAIN = "proton_drive"

CONF_BACKUP_FOLDER = "backup_folder"

CLI_VERSION = "0.8.0"

CLI_BASE_URL_FORMAT: dict[str, str] = {
    "glibc": "https://proton.me/download/drive/cli/{version}/linux-{arch}/proton-drive",
    "musl": "https://proton.me/download/drive/cli/{version}/linux-{arch}-musl/proton-drive",
}
CLI_CHECKSUMS: dict[str, str] = {
    "glibc-arm64": (
        "27a1aec1d2095fd4a1a81e1d47cd1f9fd4901bd579ffe50342d15e2e52078d6e"
        "8b2dddcf58a4a386438dc7562017778be26c1ba62399f901ae82c7430e2140a3"
    ),
    "glibc-x64": (
        "cf61c2688c45e1055d8add6221d9471a5a5b64bf3bcdb86460f5cb18414596cc"
        "4df3cdb6627c9097c94bec32a3c9915ada3211ef2ae5be33c46ebbc996ccaa28"
    ),
    "musl-arm64": (
        "fb386cab36bc346e8bae1f3e79efdd14810de748e762a2c88f384016199ff721"
        "1304cc0ec4d220c260c67b83bbe4d3a8d4dd2a2ea0e93b9fdd25c1e42f448165"
    ),
    "musl-x64": (
        "c76e2c000cc22c01842c05fd7122a4ffbccbe8c0938b8ac892a125cdcbea1e8d"
        "374be89916b6b2fddf7f1678105b67283f75a1f9a44f62df478be119b7dc857b"
    ),
}
