#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Threat intelligence module for ZeroHunter
"""

import os
import time
import logging
import threading
import requests
import json
import yara

logger = logging.getLogger('zerohunter.detection.threat_intel')

class ThreatIntelligence:
    """Threat intelligence module for ZeroHunter"""
    
    def __init__(self, config):
        """Initialize threat intelligence module"""
        self.config = config
        self.running = False
        self.thread = None
        self.update_interval = config.get('threat_intelligence.update_interval', 24) * 3600  # Convert to seconds
        self.sources = config.get('threat_intelligence.sources', [])
        self.last_update = 0
        self.iocs = {
            'ip': set(),
            'domain': set(),
            'url': set(),
            'file_hash': set(),
        }
        self.yara_rules = {}
        
        # Initialize threat intelligence
        self._init_threat_intel()
        
        logger.info("Threat intelligence module initialized")
        
    def _init_threat_intel(self):
        """Initialize threat intelligence data"""
        # Create data directory if it doesn't exist
        data_dir = os.path.expanduser('~/.zerohunter/data/threat_intel')
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
            
        # Load existing data if available
        iocs_file = os.path.join(data_dir, 'iocs.json')
        if os.path.exists(iocs_file):
            try:
                with open(iocs_file, 'r') as f:
                    data = json.load(f)
                    self.iocs = {k: set(v) for k, v in data.items()}
                    self.last_update = os.path.getmtime(iocs_file)
                    logger.info(f"Loaded {sum(len(v) for v in self.iocs.values())} IOCs from {iocs_file}")
            except Exception as e:
                logger.error(f"Error loading IOCs from {iocs_file}: {e}")
                
        # Load YARA rules if available
        yara_dir = os.path.join(data_dir, 'yara')
        if os.path.exists(yara_dir):
            try:
                for root, _, files in os.walk(yara_dir):
                    for file in files:
                        if file.endswith('.yar') or file.endswith('.yara'):
                            rule_path = os.path.join(root, file)
                            try:
                                self.yara_rules[file] = yara.compile(rule_path)
                                logger.info(f"Loaded YARA rules from {rule_path}")
                            except Exception as e:
                                logger.error(f"Error compiling YARA rules from {rule_path}: {e}")
            except Exception as e:
                logger.error(f"Error loading YARA rules: {e}")
                
        # Update if needed
        if time.time() - self.last_update > self.update_interval:
            self.update()
        
    def start(self):
        """Start threat intelligence module"""
        if self.running:
            logger.warning("Threat intelligence module already running")
            return
            
        self.running = True
        self.thread = threading.Thread(target=self._monitor_loop)
        self.thread.daemon = True
        self.thread.start()
        logger.info("Threat intelligence module started")
        
    def stop(self):
        """Stop threat intelligence module"""
        if not self.running:
            logger.warning("Threat intelligence module not running")
            return
            
        self.running = False
        if self.thread:
            self.thread.join(timeout=5.0)
        logger.info("Threat intelligence module stopped")
        
    def _monitor_loop(self):
        """Main monitoring loop"""
        while self.running:
            try:
                # Check if update is needed
                if time.time() - self.last_update > self.update_interval:
                    self.update()
                    
                # Sleep for a bit
                time.sleep(60.0)
            except Exception as e:
                logger.error(f"Error in threat intelligence monitoring loop: {e}")
                
    def update(self):
        """Update threat intelligence data"""
        logger.info("Updating threat intelligence data")
        
        # This is a placeholder for actual implementation
        # In a real implementation, this would fetch data from threat intelligence sources
        
        self.last_update = time.time()
        
        # Save updated data
        data_dir = os.path.expanduser('~/.zerohunter/data/threat_intel')
        iocs_file = os.path.join(data_dir, 'iocs.json')
        try:
            with open(iocs_file, 'w') as f:
                json.dump({k: list(v) for k, v in self.iocs.items()}, f)
            logger.info(f"Saved {sum(len(v) for v in self.iocs.values())} IOCs to {iocs_file}")
        except Exception as e:
            logger.error(f"Error saving IOCs to {iocs_file}: {e}")
                
    def check_ioc(self, ioc_type, value):
        """Check if a value matches a known indicator of compromise"""
        if ioc_type in self.iocs and value in self.iocs[ioc_type]:
            return True
        return False
    
    def scan_file(self, file_path):
        """Scan a file using YARA rules"""
        logger.info(f"Scanning file with YARA rules: {file_path}")
        results = []
        
        try:
            # Apply all YARA rules to the file
            for rule_name, rule in self.yara_rules.items():
                matches = rule.match(file_path)
                if matches:
                    for match in matches:
                        results.append({
                            'type': 'yara_match',
                            'rule': match.rule,
                            'tags': match.tags,
                            'meta': match.meta,
                            'strings': match.strings,
                            'file': file_path,
                        })
        except Exception as e:
            logger.error(f"Error scanning file {file_path} with YARA rules: {e}")
        
        return results
    
    def scan_memory(self, pid=None):
        """Scan process memory using YARA rules"""
        logger.info(f"Scanning memory with YARA rules: {pid if pid else 'all processes'}")
        results = []
        
        # This is a placeholder for actual implementation
        # In a real implementation, this would scan process memory using YARA rules
        
        return results
