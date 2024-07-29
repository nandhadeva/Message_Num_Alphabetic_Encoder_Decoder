from fastapi import APIRouter, Depends, HTTPException
from ..schemas import decoder_schema
from ..custom_logic import my_logic

router = APIRouter(
    prefix="/message",
    tags=["decoder", "encoder"]
)


@router.post("/decoder")
def decode_message(message_info: decoder_schema.DecoderBase):
    message = message_info.message
    return my_logic.decoder(get_message=message)


@router.post("/encoder")
def encode_message(message_info: decoder_schema.EncoderBase):
    message = message_info.message
    return my_logic.encoder(message)
