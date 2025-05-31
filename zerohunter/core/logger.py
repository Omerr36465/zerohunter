#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Logger module for ZeroHunter
"""

import os
import logging
import logging.handlers

def setup_logger(level=logging.INFO):
    """Setup logger with file and console handlers"""
    # Create logger
    logger = logging.getLogger('zerohunter')
    logger.setLevel(level)
    
    # Create formatters
    file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_formatter = logging.Formatter('%(levelname)s: %(message)s')
    
    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(console_formatter)
    
    # Create file handler
    log_dir = os.path.expanduser('~/.zerohunter/logs')
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
        
    log_file = os.path.join(log_dir, 'zerohunter.log')
    file_handler = logging.handlers.RotatingFileHandler(
        log_file, maxBytes=10*1024*1024, backupCount=5
    )
    file_handler.setLevel(level)
    file_handler.setFormatter(file_formatter)
    
    # Add handlers to logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    
    return logger
