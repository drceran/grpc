import httpx
import time
from pydantic import BaseModel
from typing import List, Optional

# Define the models just like in FastAPI
class Channel(BaseModel):
    tsid: Optional[str]
    annex: Optional[str]
    qam_name: Optional[str]
    base_port: Optional[str]
    frequency: Optional[str]
    port_step: Optional[str]
    power_key: Optional[str]
    interleaver: Optional[str]
    output_port: Optional[str]
    base_program: Optional[str]
    media_cipher: Optional[str]
    channel_width: Optional[str]
    max_bandwidth: Optional[float]
    program_count: Optional[str]
    service_state: Optional[str]
    qam_group_name: Optional[str]
    modulation_type: Optional[str]

class Device(BaseModel):
    vendor: Optional[str]
    headend: Optional[str]
    channels: List[Channel] = []

class Info(BaseModel):
    checksum: Optional[str]
    device_count: Optional[int]
    source_count: Optional[int]
    service_group_count: Optional[int]

class DeviceData(BaseModel):
    id: str
    info: Info
    equipment: List[dict] = []
    channelList: List[dict] = []
    destinations: List[dict] = []
    serviceGroups: List[dict] = []
    sourceEquipment: List[dict] = []
    devices: List[Device] = []

# Prepare the device data
device_data = DeviceData(
    id="12345",
    info=Info(checksum="abc123", device_count=10, source_count=5, service_group_count=3),
    devices=[
        Device(
            vendor="VendorA",
            headend="Headend1",
            channels=[
                Channel(
                    tsid="123",
                    annex="B",
                    qam_name="QAM-1",
                    frequency="550MHz",
                    power_key="PK123",
                    base_port="1",
                    port_step="1",
                    interleaver="interleaver_value",
                    output_port="1",
                    base_program="program1",
                    media_cipher="cipher1",
                    channel_width="20MHz",
                    max_bandwidth=100.0,
                    program_count="10",
                    service_state="active",
                    qam_group_name="group1",
                    modulation_type="QAM256"
                )
            ]
        )
    ]
)


async def send_device_data():
    async with httpx.AsyncClient() as client:
        # Start the timer
        start_time = time.time()

        # Send POST request
        response = await client.post(
            "http://127.0.0.1:8000/device-data/", json=device_data.dict()
        )

        # End the timer
        end_time = time.time()

        # Calculate processing time
        elapsed_time = end_time - start_time

        print(f"Request processed in {elapsed_time:.4f} seconds")
        print(response.json())

# Run the client
import asyncio
asyncio.run(send_device_data())
