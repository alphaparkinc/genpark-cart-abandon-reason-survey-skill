class CartAbandonReasonClient:
    def analyze_reason(self, reason_code: str, cart_subtotal: float) -> dict:
        return {"recovery_strategy": f"Offer discount for {reason_code}", "suggested_coupon_code": "SAVE10"}