#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Core configuration module for ZeroHunter
"""

import os
import json
import logging

logger = logging.getLogger('zerohunter.core.config')

class Config:
    """Configuration class for ZeroHunter"""
    
    def __init__(self):
        """Initialize configuration with default values"""
        self.config = {
            'general': {
                'language': 'en',
                'theme': 'dark',
                'log_level': 'info',
                'auto_update': True,
            },
            'network': {
                'interfaces': [],
                'monitor_all': True,
                'capture_packets': True,
                'analyze_dns': True,
                'analyze_http': True,
                'analyze_https': True,
                'analyze_email': True,
                'analyze_ftp': True,
                'analyze_ssh': True,
            },
            'system': {
                'monitor_processes': True,
                'monitor_files': True,
                'monitor_registry': True,
                'monitor_memory': True,
                'monitor_network': True,
                'monitor_directories': [],
            },
            'detection': {
                'behavioral_analysis': True,
                'anomaly_detection': True,
                'network_analysis': True,
                'machine_learning': True,
                'threat_intelligence': True,
            },
            'ml': {
                'models_dir': os.path.expanduser('~/.zerohunter/models'),
                'auto_train': True,
                'training_interval': 7,  # days
                'detection_threshold': 0.8,
            },
            'threat_intelligence': {
                'update_interval': 24,  # hours
                'sources': [
                    'https://threatintel.example.com/feed1',
                    'https://threatintel.example.com/feed2',
                ],
            },
            'ui': {
                'dashboard_refresh_interval': 5,  # seconds
                'events_max_display': 1000,
                'threats_max_display': 1000,
            },
        }
        
        # Create default config directory if it doesn't exist
        self.config_dir = os.path.expanduser('~/.zerohunter')
        self.config_file = os.path.join(self.config_dir, 'config.json')
        
        if not os.path.exists(self.config_dir):
            os.makedirs(self.config_dir)
            
        # Load config if it exists
        if os.path.exists(self.config_file):
            self.load()
    
    def load(self, config_file=None):
        """Load configuration from file"""
        file_to_load = config_file or self.config_file
        
        try:
            with open(file_to_load, 'r') as f:
                loaded_config = json.load(f)
                
            # Update config with loaded values
            for section, values in loaded_config.items():
                if section in self.config:
                    self.config[section].update(values)
                else:
                    self.config[section] = values
                    
            logger.info(f"Configuration loaded from {file_to_load}")
            return True
        except Exception as e:
            logger.error(f"Error loading configuration: {e}")
            return False
    
    def save(self, config_file=None):
        """Save configuration to file"""
        file_to_save = config_file or self.config_file
        
        try:
            with open(file_to_save, 'w') as f:
                json.dump(self.config, f, indent=4)
                
            logger.info(f"Configuration saved to {file_to_save}")
            return True
        except Exception as e:
            logger.error(f"Error saving configuration: {e}")
            return False
    
    def get(self, path, default=None):
        """Get configuration value by path"""
        parts = path.split('.')
        value = self.config
        
        try:
            for part in parts:
                value = value[part]
            return value
        except (KeyError, TypeError):
            return default
    
    def set(self, path, value):
        """Set configuration value by path"""
        parts = path.split('.')
        config = self.config
        
        for i, part in enumerate(parts[:-1]):
            if part not in config:
                config[part] = {}
            config = config[part]
            
        config[parts[-1]] = value
        return True
