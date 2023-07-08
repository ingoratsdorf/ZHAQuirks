"""TS011F plug."""

from zigpy.profiles import zha
from zigpy.quirks import CustomDevice
from zigpy.zcl.clusters.general import (
    Basic,
    GreenPowerProxy,
    Groups,
    Identify,
    OnOff,
    Ota,
    Scenes,
    Time,
)
from zigpy.zcl.clusters.homeautomation import ElectricalMeasurement
from zigpy.zcl.clusters.smartenergy import Metering

from zhaquirks.const import (
    DEVICE_TYPE,
    ENDPOINTS,
    INPUT_CLUSTERS,
    MODEL,
    MODELS_INFO,
    OUTPUT_CLUSTERS,
    PROFILE_ID,
)
from zhaquirks.tuya import (
    TuyaZBE000Cluster,
    TuyaZBElectricalMeasurement,
    TuyaZBMeteringCluster,
    TuyaZBOnOffAttributeCluster,
)
from zhaquirks.tuya.mcu import EnchantedDevice


class Plug_v3(EnchantedDevice):
    """Another TS011F Tuya plug. First one using this definition is _TZ3000_0zfrhq4i."""

    signature = {
        MODELS_INFO: [
            ("_TZ3000_0zfrhq4i", "TS011F")
        ],
        ENDPOINTS: {
            # <SimpleDescriptor endpoint=1 profile=260 device_type=81
            # device_version=1
            # input_clusters=[0x0000, 0x0003, 0x0004, 0x0005, 0x0006, 0x000a, 0x0702, 0x0b04, 0x1000. 0x1888, 0xe000]
            # output_clusters=[10, 25]>
            1: {
                PROFILE_ID: zha.PROFILE_ID, #0x0104 (260)
                DEVICE_TYPE: zha.DeviceType.SMART_PLUG, #0x0051,
                INPUT_CLUSTERS: [
                    Basic.cluster_id, #0x0000
                    Identify.cluster_id, #0x0003
                    Groups.cluster_id, #0x0004
                    Scenes.cluster_id, #0x0005
                    OnOff.cluster_id, #0x0006
                    Time.cluster_id, #0x000a
                    Metering.cluster_id, #0x0702
                    ElectricalMeasurement.cluster_id, #0x0b04
                    0x1000, #Dunno what that is; maybe Lightlink? LightLink.cluster_id
                    0x1888, #Dunno that one either
                    TuyaZBE000Cluster.cluster_id, #0xe000
                ],
                OUTPUT_CLUSTERS: [Ota.cluster_id], #0x0019
            },
            # <SimpleDescriptor endpoint=242 profile=41440 device_type=97
            # device_version=0
            # input_clusters=[]
            # output_clusters=[33]>
            242: {
                PROFILE_ID: 0xa1e0,
                DEVICE_TYPE: 0x0061,
                INPUT_CLUSTERS: [],
                OUTPUT_CLUSTERS: [GreenPowerProxy.cluster_id], #0x0021
            },
        },
    }
    replacement = {
        ENDPOINTS: {
            1: {
                PROFILE_ID: zha.PROFILE_ID, #0x0104 (260)
                DEVICE_TYPE: zha.DeviceType.ON_OFF_PLUG_IN_UNIT,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,#0x0000
                    Identify.cluster_id,#0x0003
                    Groups.cluster_id,#0x0004
                    Scenes.cluster_id,#0x0005
                    TuyaZBOnOffAttributeCluster,#0x0006
                    Time.cluster_id, #0x000a
                    TuyaZBMeteringCluster, #0x0702
                    TuyaZBElectricalMeasurement,#0x0b04
                    0x1000, #Dunno what that is, maybe LightLink.cluster_id (https://github.com/zigpy/zigpy/blob/a4300b171862bfdd561cedbdfd70ebd8dc251607/zigpy/zcl/clusters/lightlink.py#L81)
                    0x1888, #Dunno that one either
                    TuyaZBE000Cluster, #0xe000
                ],
                OUTPUT_CLUSTERS: [Ota.cluster_id], #0x0019
            },
            242: {
                PROFILE_ID: 41440,
                DEVICE_TYPE: 97,
                INPUT_CLUSTERS: [],
                OUTPUT_CLUSTERS: [GreenPowerProxy.cluster_id],
            },
        },
    }

