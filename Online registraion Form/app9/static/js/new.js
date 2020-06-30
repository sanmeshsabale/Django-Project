

function fvalidate()
    {
        var pass=document.getElementById("t5").value;
        var regex=/^[A-Za-z0-9]+$/;
        if (regex.test(pass))
            {
                return true
            }
        else
        {
            document.getElementById("s1").innerText="Invalid Data";
            return false
        }
    }
