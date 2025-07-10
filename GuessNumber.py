from flask import render_template, request, session, redirect, url_for
import random

def SetNumber():
    if request.method == "POST":
        try:
            low = int(request.form["low"])
            high = int(request.form["high"])
            if low >= high:
                raise ValueError("Batas bawah harus lebih kecil dari batas atas")
            
            session["low"] = low
            session["high"] = high
            session["the_num"] = random.randint(low, high)
            session["attempts"] = 0

            return redirect(url_for("GuessNum"))

        except ValueError as e:
            return render_template("p_setnum.html", error=str(e))
        
    return render_template("p_setnum.html")        
                                   
def GuessNum():
    if "the_num" not in session:
        return redirect(url_for("p_setnum"))
    
    the_num = session["the_num"]
    attempts = session.get("attempts", 0)
    
    if request.method == "POST":
        try:
            guess = int(request.form["guess"])
            attempts += 1
            session["attempts"] = attempts

            if guess == the_num:
                return render_template("p_result.html", result="Jawabanmu Benar", number=the_num)
            elif guess != the_num and attempts >= 7:
                return render_template("p_result.html", result="Kamu Gagal", number=the_num)
            elif guess < the_num:
                message = "Terlalu Rendah"
            else:
                message = "Terlalu Tinggi"

            return render_template("p_guenum.html", message=message, attempts_left=7-attempts)
        
        except ValueError:
            return render_template("p_guenum.html", message="masukan angka valid", attempts_left=7-attempts)

    return render_template("p_guenum.html", message="", attempts_left=7-attempts)