def deposit(money):
    """
    จำลองการฝากเงินเข้าบัญชี
    money: ยอดเงินเริ่มต้นในบัญชี (บาท)
    """
    print(f"ยอดเงินเริ่มต้น: {money} บาท")
    try:
        amount_str = input("กรอกจำนวนเงินที่ต้องการฝาก: ")
        amount = float(amount_str)
 
        if amount <= 0:
            raise ValueError("จำนวนเงินฝากต้องมากกว่า 0")
    except ValueError as e:
        print(f"เกิดข้อผิดพลาด: {e}")
    else:
        new_balance = money + amount
        print("ฝากเงินสำเร็จ")
        print(f"ยอดเงินคงเหลือ: {new_balance:.2f} บาท")
    finally:
        print("สิ้นสุดรายการฝากเงิน")
if __name__ == "__main__":
    deposit(1000)
 