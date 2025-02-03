from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import List, Optional

import time

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI app!"}

# Define the nested data models based on your proto definition
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


@app.post("/device-data/")
async def process_device_data(device_data: DeviceData, request: Request):
    # Record the start time
    start_time = time.time()

    # Process the incoming data (this is where your logic goes)
    print(f"Received DeviceData: {device_data}")

    # Record the end time
    end_time = time.time()

    # Calculate elapsed time
    elapsed_time = end_time - start_time

    # Send a response back to the client with the elapsed time
    return {
        "message": "DeviceData received successfully!",
        "processing_time": f"{elapsed_time:.4f} seconds",
        "data": device_data
    }