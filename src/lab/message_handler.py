from engine.message_processor import MessageProcessor
from engine.processing_result import ProcessingResult
from lab.exchange_service import ExchangeServiceAPI
from lab.models import CotacaoRequest, CotacaoResponse
from lab.utils import round_decimal

class MessageHandler(MessageProcessor):
    
    def __init__(self):
        self.exchange_service = ExchangeServiceAPI()

    
    def processMessage(self, data) -> ProcessingResult:
    
        processingResult: ProcessingResult = None
        
        try:
            payload = self.process(data)
        
            processingResult = ProcessingResult(suceeded=True, payload=payload.model_dump_json())
            
        except Exception as e:
            print(f"[ERROR] Failed to process message: {e}")
            processingResult = ProcessingResult(suceeded=False, payload=None)
        
        return processingResult


    def process(self, raw_message: dict) -> CotacaoResponse:
        pass