from asgiref.sync import async_to_sync
import asyncio 
from datetime import datetime
from django.db import connection,transaction
from django.db.models import Q
from django.db.models import ExpressionWrapper, F, FloatField
from fastapi import APIRouter, Request, HTTPException
from pydantic import BaseModel
from starlette.responses import JSONResponse
from typing import List, Optional
from polls.schemas import Schema
from polls.models import EndpointStates, ClientInfo, Client, Endpoint


class answer(BaseModel):
    filtered_count: int
    client_info: str
    state_id: str

router = APIRouter()

async def Endpoint_obj(stamp):
    return EndpointStates.objects.all().filter(endpoint_id=139).filter(state_start__gte=stamp).order_by('-state_start')
    
async def clientinfo_obj(id_cl):
    return ClientInfo.objects.all().filter(id=list(Client.objects.all().filter(id=id_cl))[0].client_info)
@router.post("/my_endpoint", response_model=answer)
def endpoint_states(request: Request, schema: Schema):
    try:
        input_start = schema.input_start
        input_timestamp  = input_start.timestamp()*1000
        test=asyncio.run(Endpoint_obj(input_timestamp))
        #test=EndpointStates.objects.all().filter(endpoint_id=139).filter(state_start__gte=input_timestamp).order_by('-state_start')
        d=[]
        id_cl_in=0
        for i in test:
            if i.pk%3==0:
                d.append(i)
        id_cl_in=d[2].client_id
        infor=ClientInfo.objects.all().filter(id=list(Client.objects.all().filter(id=id_cl_in))[0].client_info)
        #infor=asyncio.run(clientinfo_obj(id_cl_in))
        return {
            "filtered_count": len(d),
            "client_info": list(infor)[0].info,
            "state_id": d[2].state_id
        }
    except:
        raise HTTPException(status_code=400, detail="Not enough records")
    