#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Core module for ZeroHunter detection functionality
"""

import logging

logger = logging.getLogger('zerohunter.detection')

class DetectionEngine:
    """Main detection engine for ZeroHunter"""
    
    def __init__(self, config):
        """Initialize detection engine"""
        self.config = config
        self.detectors = []
        
        # Initialize detectors based on configuration
        if config.get('detection.behavioral_analysis', True):
            from zerohunter.detection.behavioral import BehavioralAnalyzer
            self.detectors.append(BehavioralAnalyzer(config))
            
        if config.get('detection.anomaly_detection', True):
            from zerohunter.detection.anomaly import AnomalyDetector
            self.detectors.append(AnomalyDetector(config))
            
        if config.get('detection.network_analysis', True):
            from zerohunter.detection.network import NetworkAnalyzer
            self.detectors.append(NetworkAnalyzer(config))
            
        if config.get('detection.threat_intelligence', True):
            from zerohunter.detection.threat_intel import ThreatIntelligence
            self.detectors.append(ThreatIntelligence(config))
            
        logger.info(f"Detection engine initialized with {len(self.detectors)} detectors")
        
    def start(self):
        """Start all detectors"""
        for detector in self.detectors:
            detector.start()
        logger.info("All detectors started")
        
    def stop(self):
        """Stop all detectors"""
        for detector in self.detectors:
            detector.stop()
        logger.info("All detectors stopped")
        
    def scan_file(self, file_path):
        """Scan a file for threats"""
        logger.info(f"Scanning file: {file_path}")
        results = []
        
        for detector in self.detectors:
            if hasattr(detector, 'scan_file'):
                result = detector.scan_file(file_path)
                if result:
                    results.extend(result)
                    
        return results
    
    def scan_directory(self, directory_path):
        """Scan a directory for threats"""
        logger.info(f"Scanning directory: {directory_path}")
        results = []
        
        for detector in self.detectors:
            if hasattr(detector, 'scan_directory'):
                result = detector.scan_directory(directory_path)
                if result:
                    results.extend(result)
                    
        return results
    
    def scan_process(self, process_id):
        """Scan a process for threats"""
        logger.info(f"Scanning process: {process_id}")
        results = []
        
        for detector in self.detectors:
            if hasattr(detector, 'scan_process'):
                result = detector.scan_process(process_id)
                if result:
                    results.extend(result)
                    
        return results
    
    def scan_memory(self):
        """Scan system memory for threats"""
        logger.info("Scanning memory")
        results = []
        
        for detector in self.detectors:
            if hasattr(detector, 'scan_memory'):
                result = detector.scan_memory()
                if result:
                    results.extend(result)
                    
        return results
    
    def scan_system(self):
        """Scan the entire system for threats"""
        logger.info("Scanning system")
        results = []
        
        for detector in self.detectors:
            if hasattr(detector, 'scan_system'):
                result = detector.scan_system()
                if result:
                    results.extend(result)
                    
        return results
    
    def scan_network(self):
        """Scan the network for threats"""
        logger.info("Scanning network")
        results = []
        
        for detector in self.detectors:
            if hasattr(detector, 'scan_network'):
                result = detector.scan_network()
                if result:
                    results.extend(result)
                    
        return results
