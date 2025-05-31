#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Main entry point for ZeroHunter application
"""

import sys
import argparse
import logging
from PyQt5.QtWidgets import QApplication

from zerohunter.ui.main_window import MainWindow
from zerohunter.core.config import Config
from zerohunter.core.logger import setup_logger


def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description='ZeroHunter - Advanced Linux Tool for Zero-Day Attack Detection')
    parser.add_argument('--cli', action='store_true', help='Run in command-line mode')
    parser.add_argument('--scan', action='store_true', help='Perform a scan')
    parser.add_argument('--system', action='store_true', help='Scan system')
    parser.add_argument('--network', action='store_true', help='Scan network')
    parser.add_argument('--file', type=str, help='Scan a file')
    parser.add_argument('--directory', type=str, help='Scan a directory')
    parser.add_argument('--process', type=int, help='Scan a process')
    parser.add_argument('--memory', action='store_true', help='Scan memory')
    parser.add_argument('--report', action='store_true', help='Generate a report')
    parser.add_argument('--format', type=str, choices=['pdf', 'html', 'json'], default='pdf', help='Report format')
    parser.add_argument('--output', type=str, help='Output file')
    parser.add_argument('--debug', action='store_true', help='Enable debug mode')
    parser.add_argument('--config', type=str, help='Configuration file')
    parser.add_argument('--version', action='store_true', help='Show version')
    
    return parser.parse_args()


def main():
    """Main function"""
    args = parse_arguments()
    
    # Show version and exit
    if args.version:
        from zerohunter import __version__
        print(f"ZeroHunter version {__version__}")
        return 0
    
    # Setup logger
    log_level = logging.DEBUG if args.debug else logging.INFO
    setup_logger(log_level)
    logger = logging.getLogger('zerohunter')
    
    # Load configuration
    config = Config()
    if args.config:
        config.load(args.config)
    
    # CLI mode
    if args.cli:
        logger.info("Starting ZeroHunter in CLI mode")
        # TODO: Implement CLI mode
        if args.scan:
            if args.system:
                logger.info("Scanning system")
                # TODO: Implement system scan
            elif args.network:
                logger.info("Scanning network")
                # TODO: Implement network scan
            elif args.file:
                logger.info(f"Scanning file: {args.file}")
                # TODO: Implement file scan
            elif args.directory:
                logger.info(f"Scanning directory: {args.directory}")
                # TODO: Implement directory scan
            elif args.process:
                logger.info(f"Scanning process: {args.process}")
                # TODO: Implement process scan
            elif args.memory:
                logger.info("Scanning memory")
                # TODO: Implement memory scan
            else:
                logger.error("No scan target specified")
                return 1
        elif args.report:
            logger.info(f"Generating {args.format} report")
            # TODO: Implement report generation
            if not args.output:
                logger.error("No output file specified")
                return 1
        else:
            logger.error("No action specified")
            return 1
    # GUI mode
    else:
        logger.info("Starting ZeroHunter in GUI mode")
        app = QApplication(sys.argv)
        window = MainWindow(config)
        window.show()
        return app.exec_()
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
