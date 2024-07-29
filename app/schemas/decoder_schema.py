from pydantic import BaseModel


class DecoderBase(BaseModel):
    message: str


class EncoderBase(BaseModel):
    message: str
