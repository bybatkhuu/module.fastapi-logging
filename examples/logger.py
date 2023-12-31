# -*- coding: utf-8 -*-

from beans_logging import Logger, LoggerLoader
from beans_logging_fastapi import (
    add_http_file_handler,
    add_http_file_json_handler,
    http_file_format,
)

logger_loader = LoggerLoader()
logger: Logger = logger_loader.load()


def _http_file_format(record: dict) -> str:
    _format = http_file_format(
        record=record,
        msg_format=logger_loader.config.extra.http_file_format,
        tz=logger_loader.config.extra.http_file_tz,
    )
    return _format


if logger_loader.config.extra.http_file_enabled:
    add_http_file_handler(
        logger_loader=logger_loader,
        log_path=logger_loader.config.extra.http_log_path,
        err_path=logger_loader.config.extra.http_err_path,
        formatter=_http_file_format,
    )

if logger_loader.config.extra.http_json_enabled:
    add_http_file_json_handler(
        logger_loader=logger_loader,
        log_path=logger_loader.config.extra.http_json_path,
        err_path=logger_loader.config.extra.http_json_err_path,
    )


__all__ = ["logger", "logger_loader"]
