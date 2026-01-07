"""
MQTT switch with custom icon for Homeassistant autodiscovery.
"""
#  Copyright (c) 2023 - Tobias Jaehnel
#  This code is published under the MIT license

from typing import Optional

from ha_mqtt.mqtt_switch import MqttSwitch
from ha_mqtt.mqtt_device_base import MqttDeviceSettings


class MqttSwitchWithIcon(MqttSwitch):
    """MQTT switch with custom icon support.
    
    Attributes:
        icon: Material Design Icons icon name (e.g., 'mdi:lock-outline')
    """
    
    def __init__(self, settings: MqttDeviceSettings, icon: str) -> None:
        """Initialize MQTT switch with icon.
        
        Args:
            settings: MQTT device settings
            icon: Material Design Icons icon name
        """
        self.icon: str = icon
        super().__init__(settings)

    def pre_discovery(self) -> None:
        """Configure icon for Homeassistant discovery."""
        self.add_config_option("icon", self.icon)
        super().pre_discovery()
