# Error Handling & Logging

## Overview
This document describes the error handling and logging strategy for the Simple Model Manager project.

- Comprehensive error handling middleware
- Structured logging using Python logging
- Error recovery for translation and file processing

This file will be updated as error handling and logging evolve.

## Error Handling Middleware
- Custom error handlers for 400, 404, and 500 errors return JSON responses with error details.
- All errors are logged with structured messages including URL and error info.

## Structured Logging
- Logging is configured using Python's logging module.
- Log level is set from the LOG_LEVEL environment variable (default INFO).
- Logs include timestamp, level, logger name, and message. 