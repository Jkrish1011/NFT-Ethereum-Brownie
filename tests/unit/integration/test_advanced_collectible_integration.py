from scripts.advanced_collectible.deploy_and_create import deploy_and_create
from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_account
import pytest
from brownie import network, config, accounts
import time


def test_can_create_advanced_collectible():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for integration testing")
    advanced_collectible, creating_tx = deploy_and_create()
    time.sleep(60)
    assert advanced_collectible.tokenCounter() == 1
