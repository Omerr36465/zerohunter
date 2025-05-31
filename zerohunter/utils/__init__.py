#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Core module for ZeroHunter utilities
"""

import os
import logging
import platform
import subprocess
import json
import datetime

logger = logging.getLogger('zerohunter.utils')

def get_system_info():
    """Get system information"""
    info = {
        'platform': platform.platform(),
        'system': platform.system(),
        'release': platform.release(),
        'version': platform.version(),
        'architecture': platform.machine(),
        'processor': platform.processor(),
        'hostname': platform.node(),
        'python_version': platform.python_version(),
    }
    
    return info

def run_command(command):
    """Run a shell command and return the output"""
    try:
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )
        return {
            'success': True,
            'stdout': result.stdout,
            'stderr': result.stderr,
            'returncode': result.returncode
        }
    except subprocess.CalledProcessError as e:
        return {
            'success': False,
            'stdout': e.stdout,
            'stderr': e.stderr,
            'returncode': e.returncode
        }
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }

def save_json(data, file_path):
    """Save data to a JSON file"""
    try:
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)
        return True
    except Exception as e:
        logger.error(f"Error saving JSON to {file_path}: {e}")
        return False

def load_json(file_path):
    """Load data from a JSON file"""
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        logger.error(f"Error loading JSON from {file_path}: {e}")
        return None

def format_timestamp(timestamp=None):
    """Format a timestamp for display"""
    if timestamp is None:
        timestamp = datetime.datetime.now()
    elif isinstance(timestamp, (int, float)):
        timestamp = datetime.datetime.fromtimestamp(timestamp)
        
    return timestamp.strftime('%Y-%m-%d %H:%M:%S')

def ensure_dir(directory):
    """Ensure a directory exists"""
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory

def human_readable_size(size_bytes):
    """Convert bytes to a human-readable format"""
    if size_bytes == 0:
        return "0B"
    
    size_names = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = 0
    while size_bytes >= 1024 and i < len(size_names) - 1:
        size_bytes /= 1024.0
        i += 1
        
    return f"{size_bytes:.2f} {size_names[i]}"

def generate_report(data, format='pdf', output_file=None):
    """Generate a report in the specified format"""
    if format == 'json':
        if output_file:
            return save_json(data, output_file)
        else:
            return json.dumps(data, indent=4)
    elif format == 'html':
        # In a real implementation, this would generate an HTML report
        if output_file:
            with open(output_file, 'w') as f:
                f.write("<html><body><h1>ZeroHunter Report</h1></body></html>")
            return True
        else:
            return "<html><body><h1>ZeroHunter Report</h1></body></html>"
    elif format == 'pdf':
        # In a real implementation, this would generate a PDF report
        if output_file:
            # Placeholder for PDF generation
            return True
        else:
            return None
    else:
        logger.error(f"Unsupported report format: {format}")
        return None
