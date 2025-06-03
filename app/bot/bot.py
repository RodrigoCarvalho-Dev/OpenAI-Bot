import requests as req
import os
import json

class GeminiBot:
    
    def __init__(self, api_key: str):
        self.base_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"
        # Informações da empresa
        self.company_info = {
            "nome": "SechPay",
            "telefone": "(11) 98765-4321",
            "celular": "(11) 98765-4321",
            "email": "contato@sechpay.com",
            "horario": "Segunda a Sexta, das 9h às 18h",
            "site": "www.sechpay.com"
        }
        
        # Contexto inicial para o bot
        self.system_prompt = f"""
        Você é um assistente virtual da {self.company_info['nome']}.
        Use estas informações quando solicitado:
        - Telefone: {self.company_info['telefone']}
        - Celular/WhatsApp: {self.company_info['celular']}
        - Email: {self.company_info['email']}
        - Horário de funcionamento: {self.company_info['horario']}
        - Site: {self.company_info['site']}
        
        Seja sempre cordial e profissional. Se perguntarem sobre informações não listadas acima,
        diga que precisará verificar com a equipe e sugira que entrem em contato por telefone ou email.
        """

    def get_chat(self, prompt: str) -> dict | str:
        try:
            # Combina o contexto do sistema com a pergunta do usuário
            full_prompt = f"{self.system_prompt}\n\nUsuário: {prompt}\nAssistente:"
            
            response = req.post(
                url=self.base_url,
                headers={'Content-Type': 'application/json'},
                json={
                    "contents": [
                        {
                            "parts": [
                                {
                                    "text": full_prompt
                                }
                            ]
                        }
                    ]
                }
            )
            
            data = response.json()
            return data["candidates"][0]["content"]["parts"][0]["text"]
        except Exception as err:
            return {"error": f"Erro ao processar sua mensagem: {str(err)}"}

        
        
        
    

        
        