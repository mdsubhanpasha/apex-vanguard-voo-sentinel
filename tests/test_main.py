import os
import json
import pytest
from src.main import VOOSentinelCore, MOCK_TRADE_FEED

def test_sentinel_core_detection():
    sentinel = VOOSentinelCore(ticker="VOO")
    metrics = sentinel.analyze_stream(MOCK_TRADE_FEED)
    
    assert metrics["system_id"] == "APEX-VANGUARD-VOO-SENTINEL-4050"
    assert metrics["duplicate_count"] == 6
    assert metrics["total_leakage_prevented_usd"] == 702.90
    assert metrics["detection_accuracy_percentage"] == 99.87
    assert len(metrics["detected_duplicates"]) == 6

def test_no_duplicates():
    sentinel = VOOSentinelCore(ticker="VOO")
    unique_trades = [
        {"trade_id": "T1", "ticker": "VOO", "price": 400.0, "shares": 10, "timestamp": "2026-01-01T00:00:00Z", "broker": "B1"},
        {"trade_id": "T2", "ticker": "VOO", "price": 401.0, "shares": 10, "timestamp": "2026-01-01T00:00:01Z", "broker": "B1"},
    ]
    metrics = sentinel.analyze_stream(unique_trades)
    assert metrics["duplicate_count"] == 0
    assert metrics["total_leakage_prevented_usd"] == 0.0
