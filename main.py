import darkdetect, pyautogui as pg, PySimpleGUI as PSG
from time import sleep
from threading import Thread

def icon():
    return b'iVBORw0KGgoAAAANSUhEUgAAAQAAAAEACAQAAAD2e2DtAAAodElEQVR4nO2deZgcV3mv36+quntmpNlkWYstS8Z4t2QtI9kYY2M7IYFwuRcS4AIGEiDxEoed5GHHOIGQhOAn3NybEJwEh80JkJtcSPIkBLxgNiPJDuANG7AWW7KsdbTMTHfVOfePqu6uc6q6p7pmJFnj8+qxZ7qm69RX53x16izf+R1wOBwOh8PhcDgcDofD4XA4HA6Hw+FwOBwOh8PhcDgcDofD4XA4HA6Hw+FwOBwOh8PhcDgcDofD4XA4HA6Hw+FwOBwOh8PhcDgcDofDcTyR423AseEiIAI0XuuYtr4jrWOac/gh9x8r444rzwAHGEMjgPh6nh7waokPaK0MH1CiQCumqEcTvoa9LOQHx8XiY8mcd4Cx+Mk+nRdwKWezgErrniPjixoFaCZ4ikf5Nt/gSYBNx9bcY84cd4AxQAb0G7iBc1K1//Q0+AE38nUQNh4t454WzGkHWIfAAB/mLVRLnL6d6/mawJx2gV6eihMOhQevKVn8sIyPs0Zbb4q5xpx2AJ9omNeXLH6Ac3ibVOd0Fs1tBwBZxpkzSuAyfcosmfI0ZY47AIsZmtH5IyyeJUuepgTH24CjzEn0pz7t47Ps7drw1SzgdYy2Pg8wcrRMe3ow1x1g2Kjj9nEzj01zxun8t5QDVJl3NMx6+jDXHWDQ+ux1H9oZs1+KnlGDzEHmehtg/oxTcA5w4iIwMONE+mbBkKcxc9oB9Gw8v84BTlTORM9GDVCbBVOexsxhB3iUk1wNMC0FegGraeATEKBRCB4aDckse5rmZ239PF5zTuPZ51fFM4RdUNbn2rRn9ITm2OVGfC1Jfp7LXv418x3DATrd6H1c4AXgIfE/Ee3R/EziE/HPmOZPSe6181/SdVCgk2Pit462f/PET27Lw098K/VX/MxvEtVYYd3taURdaz3FadZDcTLLeyoxnQk1Sh/XaDQefiv3Elu19ShKlHHFbqlnvxtfSaFQhDSYuj/0WI/G7Ai3TIgLX4n3LM5iKSOM0E+NGjUqCD4efu7PdjFIkvWCn6TrJX/x8JIjfutn02n8lg2S+xtd/5r9Le1SHlWjuEN2EWayyiRgkeECh9g7zRlpBNVh+lAnMWkRGp8qQcpVTaub388r6ny3gCjz7bjoI0Ia1DnMONvYyF1sA0XQinVKsm1tnINLuZarWUZtbscJPGMJeYC/lc+qPR46qQcE4qffQz2Hj/H842mf4xgQ8Z+8n43NQBeJ42YU3q/wZzOcOnWcKPyEtzX+rYrwA2Q9Cg/9Am5h+fG2y3HM2Mo1+t99NF4E6FXc7Ir/GcVybvZWK8DzkEE+xAXH26LS6Nx/c5HZvc/z9IcY0gQa+VVeYv1R8Z98u0DyYYdOiY2gCQub26kjlUenbpHftbd/bDC7edPjp0ZJoiQPdKuDl3+nAZL8X5Lz498DKlSpUKFCjWEWsoxlVt/uxbxMbg28BfrXrbDJPfxvPil7pusJztUH7cQmHvlTCIcZJBIR8fB0jVN5FdezKPXVKr+uvypjL+KLDKcO7+QG/i9697TBdEIf+hmweOrE4RI8DqEICFDJEHCbLaz4H/wFS1OHDvDqgIuskv7yjn9cCmw5+vY6ZpnvdvnbWpYT/HN4FW9JHRxig8dZxpsh5M6lzP0Vcc887kUI4U5jKFw4y+Mk43sHeMwV/9xkE8AWDhgHT/KsF8B4T1MfjhONfYwbn4cCK2bmsD54LO1xHEs0HJTDxqGBwOoCHmGyWxKnU2cRFdLaCh5CSITwXwWMWI2iimd09T0g5Ff5JncUSGENEFHBMzrGPooq3RtCTc5gEB/fuAvBQ9HghwXOXwUIVasjLERohPumOftMnuAcApTVSveImMLnR9Ne/0I0NSRnuCQi7K5sMskR43M1oGIcOCw5gzBNjY0YIUpFeMSxCPEYRBxToIHN1vlZQ9PjNArB559b3/TQ1pLs9SijrRpHJ6XTiBDqKRuGDGdaj2TGLcy70EQIlZYFWB3cDYTG9SSJjmqjk3Gf5t2aLakxVvHjxILhzNUhXsvc3zq/gWe50jpL4EblhBAEBMn5ecvaBSLMGqBi1wB1sUZ31sVG+yxjBYuZT5/ulwqebo1ySYTSIZMcYh9PsJ1dotYhSQaMoWP3GeZ0ljFKP/30ieigXaISoqgzwThPsY0nooPCGLRSAA1VTmEJJzFEP326RiB+OopGGkxxhP3sZCuPS+MgY60iGIuzawGnspAFDNBPHxUJ8HXKj6XOJAfZwza2hvs82vewDlBQ4RQWs5Bh+unXVQkwLCBlgX5cGmuR5EGI43B+hAxxBsvjPJBqOg8BLSENJhlnN9vZVj2gWYeXFGISruOxjDNYwjz66RcvnYfEj/8UR9jHDrbKThW287B9FerG50wNMIVKe8AYmj7qq+QaXsgi+lICK1kUdY7wuHybvx7YOJEqAObzcn6D85lPtevwaMgk4zwk/8QX2BMf2hA/uSvlHVzJCDUqqRiiLA0meIrv8WnuQq9nI0nm9cvV+k08mz5qBF2GiRVTHOJR7x/5jOyOD61Hoz0u897I8xilr4gF8l1uadxV0evYTBIbOY+X6jdwIYNWlJJNxBQHeVh/mc/K/rgskjrlPP9afoUl9FllZlNngp3qbm4JvxekSwEQpU0HqARWgdSVTt+bT4N60UgBjz76WMAqfnnizfIvKjFdRvkTXldolX7AfOZzCldyCW9mzxibOIuHkEv4FKsKnA8VKgzxbK7kWv01BawF6OdG3loowNujn35O5hLW6Bsk6TIJXM3HjWHU6S24qnatfC0ief5H+EPeUMgCnwEGWMzzWM3bOTjGpnhM7xf4X5xXyIIqVYY5h18Mfouvm76m7RrA9yxvnBJjyiHCW8qHew4UeRYf0ktj2TWB1/CGHkUahFfx2vjXh2AxHytY/G1O4Xdl1CN+1/LqgsWf5pXy35uvH72cdxcsfsMCvcAjyYNf55oeLfB4HS9uidct5SMFi7/NCn6XYXMGSWumzKvYDlCXVA1wMcAYK3u8MMAaLoc1CLqfF5eYmRN+VYbikGO5gueWsGAtq2GMCmqQ15ZY3lHhxTrQcQ2ylmeXsuDC+Bc9zMtL5EGVl+hKYsHlrCthwUWsSkoxQZRVA2QdAJ3u4AHnlloaUeHiIO6mjHJGifPhLL08sWRVqTXMg1wQ91Dk5JKhbufKgtgFOavU+qDBVpTFspJ5cIEME1uwfpr3fj5DrISn0kdyXgFmGyBKlX/83aWU41mNWgVgQUmNjlGWwCUAC0tacFrSbRosuUBsEcMgBLCkpAUr4AqAJSwodf4CTgJBVXlWqfOFFaTEDmiqIbbx7BaxSvf4Ndr3Roy/h+wkzG0Da0YMNY2F0scUMN+oQRo82fH8CotTz3qFhSDUqZrFt48DHdrgtgUnSTxW1G84eciTNApZ0McQCKFnqYTsZ39HC4aN/D5J8xl+DUaNOqybBQGLU8/6QGwBNWvGppMFmoAlxrUWaM9s1U3nAHooNRYsiC2QsItXsT33fRbxTmOqcTC5kZpReW3ntTyRa7xiBZ9nWerigzBJxbcs+DR/3uGVoHg7b019nkeeA+zkNWzNvQPFcr6QssCP1UG0Z9Ugt3Jzhzd6yO/we2kLAnmFxtYp2cnVbMlNQXMKn0s97VXpT8ZAzFr0Vj6R251WLOMfSMtazcNPF7nSXsYBzMJQ4+YBsd49oWzR23MuDVjTSH1JMZkdzYjtbM0/XSMN48o1EPCs4h5nW4frwz7jU02LAFSs1UFbOlmANiZL/bjvokXMPNjbJVjCnGqphD6hQNXI1IbeIp1SMMPhAl1JLDHbYfs63YFE2lz51CepK2su4EHTAcR+llRklrjtAODli6eO2Wsem65lRucFVPOnm9fZi6PaC83MdKuCsoaaO1jgS3OBmnm8g0xMRh6G2AJPtNmJlfzz1+JjfbNpgf2YebrTHVQNd2+OFvtWI7SDBevz7sC48k8zqwjtzFHNdZeWCb3TTNm8gt9DoKRO/mc5QOHVtdn1hb2RuJ4uuIjeA7BdpfkQFMXMH2nlYW/hpekUjA8N2wEk4wCZ3Jph9tlPZQ9dOg2CZ9cAlcIGec3FxoWvmEmBnlIQrPqyaXux2GmwX5jtPJxpKSQfoukdwD5/BpfOy77iNYBGJ/+zHKDR4YQcC5o/y91Dz9mvxK4BklOLO4CdP3kPUS9YdZcUqQGOarB3LzWAynWAalA0O0SXz7hS6EwNkExB21P/nZntGsCyL88BTJRpqc7urNLL9eL/p1PopQ0QJXduWlApXKyzt3ChYDpiN5l1UnLFF7qYDqBz87AXtPlh+hoAD6uKLV592ZduGp+meA2gaeS6frcJaTsF82ev5N9BF7IOkCRRfFWU38EBymK4Tk4yWQewatyZ+F5+DVDcAcJWQyBN7w4wExfo6XxttwGa91642TLrNYBRo3s5yWSKQxvtBknPDfVGJwfwY0UCLwlqChnG4/a8FBogoC0LqgiswyMOygoBnR+NONMaYJoU1uET4iehWRqyoybN83JrgDMQBqgRiwYlX7Bfkc08LF0PT/O0ZAaCtOkAOrthRqQ7iUmZRtaTz6GRgs88fHy0KHSoPV3hEMm8u72J0xQotPLM4zX6taDRntbqEX0eIS2LTAsaOr79hpX9UUc5LPNKKh4XFK3NJ1i3QrQI2Mt88T0dy2f1WSN2zQWdU7YFkqQQUMcTLSJ4SiRinjVuGiY/TQs6aJ1pMhGdUTrEz8+ZhsmpkNOTQWgxpw+H9bs6TEQorjI+TyTGTxnDqwEf4I0S0YhCGpWQUDUIadCgLkPGGkXFYWigoj4zhOEiPid1Qt0IQxpnho2QVgpcZnxzMsn2KaNgR3gn+zpMpYwa0z4qiZDWVqT083gPVSoEVFQwUiFQFYJkPe4G45tT/VFIAw4brjksNzAer90NA69C4AWqQiAVfE7FjjIEiJgw0r2K/MEprUeMPIR62vUEjR3zaQ9SolMuKOjICiMe5m05F87jgK6DwBTmCP/FHc8wqXMQfsR6ba1UWJRZzN6J8aTgDxkuOGJMGHUjJL6ywrTgBbygqAWH9Q5OhYPUU62DBcaEUTeaDlC31vM8v7CW05F0vZrXBsjxo/YhAcXugpey2Zl47UHLe4tygP2J3OvOkhbs8uLmw34OlTr/YDy1o1W8g2AJnvQ4F7LrcYoywTgIcqR0HuyWVDMwzCnuzJF0GyBE4MGS22Y9KKECeJJOs4fd2cFOeBTgkVJNoIhHNbvR6H1d5g+7sZ298FOAn5bKA8UjxKsTnmRHOQtkl+ChQx4qdX7Eg+k2+GTOIEzXGqAG8I3ciavpONBcl6EP8NUS58N3dHNyd3Op7NvBZhhE8PfzvVIWfJcDOg5H2lTqCXyCe+Nfor18p5QFX9UHkuK73XoJFGMz37Rq9AwZB5DUK/v7TMB23sfjPV/6C9wD98VjT58ptOLL5GfcKjppfjzMF3s+H27TD2vuBxR8np+VsOALIDyKIA+VsuCL8rAAO/A1f8fPez7/Dm4F4R4E+X4JC7bzPtm+LzVxXKQNoH1j7VAfMPh1rmfztBKrTUIe42P6g3HLeTOC7OBt/CuHCvbHNYe4nev8zZoBQCDkj/hjtvZgwVb+SP9R3CXahOK59/Lb3NlDS+AQd3B99d7mrLuOyljAH+tQA4sQlm/kOu4obIHmEP/C29jRXCKnJ/UH+BhberBgM9fP/3pkdGu8nKF9GTOX6f2+98EJfpw6EEfGy6lcyRjLWcA8ai2l3ygRIg4JmeAw+3iCB7k3etRXEGffWByXNcxazuc0RphHlSAz4hURUecw+9jCj+WHel9zheHa2DyfM1nLWSxmkD4qmRnyCEWDSQ7yJD/hPh4lIlnqGcdTyyirWclyRplHFd8KlUhbsJUf8cM4umgTcDEhgvLlTNZwdlELvEdVBHHwzHpAwygXsqqjBREhIXUOs59t3M99HKhTYXOrDDxPn8lazuMURplHf9L1bGoOxyrFUxxmL1vZxO08bq/SXI+G3+f9qUMq4wDywbq1QnaMpuC4riUix+l5boVGoXWkQ6lLkpuCar4A7YWdPh6eFjFHnJVolETxuiQhxDdW9jW/rEkyzjofrbVoIonSDt5MYT1B68UWie9rD7GnwbRCi4oivzUkF7XOv5BKywZB+/haxJqm0BqNlkhHre/htRaYtu9B44n28bRlgdaiE3nnhIBGq/jWo2nO03qoKgE+gpdMuntJ0hpFSF2mkvKy4oYupoFYDtB1ICgmTuQiQmTKWldinSUs5BDftv7SDCC7mBqHaQmg5aDpR2UWeLdv4jmE6Eh3aZErtnJWJoWmBWMIvu5Wjfo52UbrgbiER1iOdLkD8KjkLFFvpngJHpNdLYB5TPF961jzDi5lHnugbkX3WygC7sk5ntcIzJkLyJ+tyUuwN+yb6p1ijfnOAxczlb75btfUi6YwE+yHqzd8spt8dO0GOuYWeYsR7Olg3akGcJz4HMbP9AJyHvdjHEflOGYUbAMUWcm9hoBGIkvbnIXVqUvEgqWaKaSA5k2bsxmk6ZUK3YosVSzhcOHxpDF8JqkiqFRqh/B4sOD5gsJDJRVkLL2qqBRuCa1DJzpGzY22IJ4hl0IqRE3+T+ZInghyiCYW7rmha2qFAkIkp4G5gWxkmKaS9DpiozZyNtCXuE+deJugPuzogUXsttR31jJkjZBEiSUeuvX7Tpr94Qn6M6PTSU87lUI1yfp2avNJz6LbDcIxmruhxXcXd+PiBr+Pn3xqnp9VMbJn6AU/sb59FxW09T3Tir9ir7mUM0kp/eSqnC6En1gLn2od+wmreX3me1kyDuCby4lZH/u+qFGGGWaEQebRR42qrlGTaiVACJD1/pDftq8SEVKnruvUmeIQhzjIOHvZveuQsB4veZbW4qM5DEM8ixWJglAt2R8s0EIomnhR8yTjPMUWtg0chLGUnlcyVFVNFHyG6Kefqg7wxaeCSoIkwmSQ5HG2shO1Bq/lRmNx7eXpRSzkZE5ikAEGqOnACzwPUDqkwQSTHGQvu3mCHTpcT7qDmTDI6ZzGKAP06xqBeKADkDCVygF2sY0nOByPkcRW3EKEZhQGWcaSZLCoQkBFVwwtIM/LlKMOtSZkiikOc4Cn2MGusw5P8JcI16a+V6gGMJ+kdUAD//zGm3geS5hPJRnF66WroImSoI2DPMRn5J/UZLMj7QEyoF/KG7mQQSpdY4YjphiX+/kc/8CRpuFjgPj6Mv0mLmV0Gg0hTYMjPM5/8in/wQaxgs/FKBScHV3LL7GEWlcVoYg6UzylvsWtfFtHa5PhLo1APy/jDcl9dGtJN5hiPw/wZf6BA01TI4A+XsqbWJnkc0685rRESeqPyDf5e+9nmr/kutYfg2w/IBMSZrUB+pjCv4y/mNGGEkKQZMgCVnC5Okd9NF4Gug7QQ3yE3ywkQhGr5yzheSznI+3gJ/H0dXzYWkDdyZIqVUa4gEt5feXBODPuYyWs5m8KaXD49NPPCGfxEv0h9an20mtdkw/w9kL3UaHCfJZxFZfwDvava9ZEFd7N781wr1Mfnz6GWcEv8nJ9A99LF7AH0/YCrIVwUzDMB2Z1P5F+3uxdJMlb24Orua5HDZIa17MmkX8C9Pm8u1Dxp1nPddqL82IVXoW39yzBcjLv8c6LXehFCFzKb/d4HwGv16+OB3hvAbiYN8/qZvXruEmPpActK0UigjK9gJWFg7iKclIzoMlDDfLKEgMPS7gqNv0ygIuNFfFF+QVJdD806lQuLZHCMp4bNz934iPPt6LxiuDzCj0Y66QCV5TUEenMc2UDfLrrV7qOA1wBcD7zZ9UogHMJ4radPpWzSqWwKm4tHEbg3FKDl6eltsk6lcUlUhDObnY0o4BzSqQA58RWCARx9NisMo816Y9P5UYEZYJC27XQOMBpR2Fs+JQ4fl6QU3P6PUU4La6oBPyeBdxi+lP1xuKSe4QvVH6SfZWSWkoLWlZUStVj07F8KtWBz9Pmyal+268AwScyq6WQJwoHJaQZNQp6mEoSKrrAyPqQHR1X0ZgpDNEnEwC6YlW9+yydkDYVlqbu10+1G0YtFaGiVox4laSLX4vlZHq2osbJAAJVbcrAdE6hGwGnGGU6Wg3a5ZXXBsjpBaTzMwoYNP7cWSOoG4p3GOHktZbixaiR1hO8lsc66PdkUmhN3JsNp1v50w76Ocu5LaUA5KWKbL6l4fPqDipCEe8ygsoHWlrDfZaGx618osN9nM7nUi8fibNbp/OkewrdUCzjy0ZN0i9+2wH85FJpcmqA9iENIqZZoWzrqBHUjf3WJZpLqMzCC9mWH8Er6E4peFb1vb9jFLJYdVf7PLPd29EKMipELVez1zx2jkT2LSuaAlS2aO/+UrHMdqyBsZKymq0BskvD/JRIucQbsJt00Ajqxjqs+J32Cjj73dtBv2e9PZPRFri0LZTeFIAAe1V/NxUhS6ug9dkuvuJWBK2fZlkIxiheET6VTd2wt4+J6eMBhEfSn6Tr2FxZ2sVXRv8S0gPkUnr+up0XZe+xPWJYXsKhee0y4349kjfNN81bJqPPMTuki698Gs2fZYvPy/mtN4KUFWXvZOYu1A0jzbynbfpbPzp+2Uy1bNZL6reZK2iVf3pn7sjd123MKnmBhDkjgaeaB45uDTDzFGbDAcriz4ITzdyFumGIK+T13zONhojnWEnMsklmqjNPvbwDzPzas/HePjr5m5v6ZG5M4HSU1aboxszFW9qUL4SZWzEbDtDM36OzF7ehEJJTA+icXkC6qytHx6y0eMpMOZ4OUF5HNWvF0crnVLoNJPOqybmB9COfXUs2S2Y16brAoRD2lhdlrDieDtDO7qOR00b9nXeBwF4rIKaeg86MinfWCCpsSMoWe5vKDvo9uvOryH7+dUEFoHSKdtqdVYTMPOzcmC1uRfMRsEtHpSP8CmOnbugj1ZmXuUzOIIqxvbTSpr7HsH5nx+0SOqO40jKzmeXjhgOO8nb2dBhDvzLnKGTfnVfk7KgYf2/U2vghzPkNYIR3dFARUvEMecdrt7kS3eE+TrLmPw+3/mK6YacUuqGxNYImdEr9uVYsJrCdGxoVeZYD8PYejcojbNUr+4lSNowW1u9p07CK7wqrkDozmfMbwEhhHaSw46xhUStUq8lV/j66MeFHbb9ayHjGpzLdQDEcwNdHZTfxydZ7ZldJ9Zw2toBSUaLUeQdK9nX2z7gNM8EuAEEmSmopdWdvlG3nG3RtBAq6vEZQN7a3bnZrSfWcRDpRkMMFV3vYTKVm27Z13zK7Iw/qdgVergm3q7X7yERJLaVuRDwkqfLMXxtokZaI2QzIXTwwy2Y1+FqsPqhRu/hWiRQiviQ7BNiIDrmtVOjEfSkdjB8V2vjcZh9/L1EyM7qDL5V6UL4XF7tG1/laD5KyxXiAu9JzijnVXLZ+0NYOSWoLN5d8PvJR3MJtceM9wIv4VIkn+G/5QzWlgQsRvG/yZz2PJ2zjw+xqjcLu4saeZ99DPul9U5Kt5JnSH+Vve0wBtvOX1PtJujK38elZHXab5GZzd6NC4wCRFZoq6C9yUw/6ON15kt/X7+FQvKZmEoXcxzXc1ZPvf4n3Mg5nEEs3qJA/5Ua2FM68OvdwzcR/NBU3NJroP7iWewpbodjKjXxchfBj4nuRg7yXLxW+B8V+vs5vBd8SJoFrAA7p9/IHpTUJTUK28uEiwlIyZui3cJP60BB3pg6MAXiczRpOZ3G8dTo1fHw8fDzipWFeMjEiqQmSWO4kImSSSSbZzyP8m94Y78Qey0WsAwQW8XxWspB++qgRb1vkkbfCR9gmH9FbFdWW4MQYoDzvbC7hApYxyiB9yeZLTffWRIRMcJA9PMYPuFvv9Mgs7FrKpWzgdE5ikP5EhKV5JxASby+/j+08wHf1w6LaQR8XU8dDluv3cVpOa0AToRB0slBuL49xv76f8bYVn6QGiK/HeBFnMUIfffQlgSa+cSe6lWKIJkQRoYiImGKCCfazi8e4Vx7RygwqWU0FfRMfSB3KaATdpD/UZ4natQc0PLSnfe17HhLLI+t4VxQhPa+dvnGIlXOURKrhhXHHOb20c4womc1RiIefErDPH20IaSgCY4FpSoGnIrGKUZyKn7zilEQoFCFTquEBVUIrBUmMlUqyNMzTSbZL7Mixgk+o635DJbeWvo8NsQ5np0VhSWWjtbR0jDR91I3oqr9KLhMEqpI8YJI8VnZKsVPqZCQi1ifSWhFJFCmvlX3XGEZcSDXjANOsDYS2l6+jga9Q0sgKjUxPLCommXW9TQUiIcwOhuTiIdb64jiNDSho5FXjaWsrNDgzU1dvAl7BI1RQuSmk0wpz7gJ+EC+jneZsSNYR5obVXQPcQkAUln/hagK0VfBNIrIbAtkOINLxDsoIhhZl5gpEWE7RjXtzjxZ/gefTa6RkPr85K6kUJ2cc4OhOUDuOH/PibZgMcsYBZn/cx/H0oNDi0KMTAeJ4OhDltN0KNAKPBstYiKaCoKgj0JNyTq+spNq1bdZdl6IIurOCZoIPqRUXx4f8eAALydQAa3ualWyen20yXsS5PJAyQlBovGSScgzYxEpDp7jNFdamHb1T69JzUTN+7UnX9JvzxkXiKHwUfdydOb6hp5gxTQ2VkpqNyRsKzlkbaD4NY/FpFZ7NYgYYoI8g9a+tcDLFYfbzBNt5UhSMGStj1uIR8mO8YU5nBQsZpE/7EogQasUU4zzO5g1PRqzL7W0cQojEW8oCBuhPpJaD5D9fBxL32Zv2tIWcW0e03yX7fJlpFaBiZfAuNGgu3Ir/r2hQp06dRjI8dJgjHNTjRBMp7aCYpBQCzuBMTqYvWRrXFOxWhMm/SQ6xj73srh+EiLVGj0cVeAVIZMgBrI2jK87lXbyQYbymVHOHpZMNJvUTcjd/M/H9ftanOkYewHx5uf4NLmA+1Rxlkkn+S73f+0bHwJ+Kdy3Xs7g1zJP61xqMOuqR9bOKSoS2VSISXWec3eox7uAr7E5nUFJzrOYGXshCqjlxkBoVj2kT0WC/bOFOvtj/0JTxQCn8zD5y04hF+2hYxV9bu2HlE+vTjHA+L+x/s/5/7XQ2oGBE/oTXdxQhFPp5Dp/UL+Mn2T9uQKFfxEetlconOtloxkWcyXP4nzyPGxhv16GChl/iz7uIaTSD4+PFPyOczvP5tcZ13t3pS+TVUdN0AzUM8P5CxZ9mOR+UU8y3Pa/hjdNqUJ7PVfmRWAIvmWPF3xnhVfrqdHWtYSl/0LOWygW8Tw+apZkXD5BxC+vAGn6pxwsDrOZyWn4T4fXxK4Xakrk6OwLeM6b4AQJeLUPNclgDcHlLE6sXLpHVkmp65r1eu44DXAxwAUPZ70xLwMVGXTLKswucdSi/p7QR1CyNtJ4orGgL3wgS73nRO0NcmI68r+W4QM4rwAoJW1oy9v10XUtVOAsKudFt8q38dpyGL83ChgMnDv3tutBDV3lWqVSE5entjCs53d2cyaD2lxr0M2kq8IXs7DhTNWKEXS+kLzU6Ms/SAkqnolDU2cvt8uf6SH5nSsMWeQu/w3CiVBp373zj/81Z0HxJXHsiTHKXlBwdPYQiBCxJlUbFEIypWTqI+y3FlU6pwALlpcQss20AHXRrAwh1zxI/2sUrO2gERbzTCKceNJaj9xmfTC0gjZJIH9l/YIROuxUIGrlH/Ybna1887cXz/EnsQNIFjFVIdG4XNS80VvIXlR2f/TJs7aDAaDBXrfrzMx11kGyNoHnit6t0lRMSlnGA9GoEjfYtEZduGkH7jU99RlmaEiq5KjwLyO7W02QTa3iKRQo164GTTxdM7SBTMMYuhY46SKK1WT8bA5RFRgI9ayhYsio++RpBGf0cc1tqW0OngwpPZ+6DkjvAngjkaAelP/uWgph0VFLKKhB1FwXSdjfQs8qx/PJHs4I9Bgo4cwqxcq+8CIZRA3jTOoCYC+tkJiIursjLY+Ze+byUzEfzSLYGEKMROIMaQCxPcu5QnvJ5Z1XnavpXgG8vm3c1wPFg1mqAdPEKjUx5Zpoe5vqxGQhE2NPXLtSwF8zcK6/Tos3SrE1fA+zPmlLy0rbUiKM05XNPmVWHn+MAZudQBkzX07kzCMWYHR9+ZjJrNUD6TEHsNp2yHcCrWbK+pS9tphs5B+gJZc3Kz0op6GwbQAVWQfm+fY498t9ZI8g0smEkZO+43VmF55mKnT/pfLfHP1UnJSWxZ3tCs1SUWMFvKrAuXI28dCKiLN2KEf17HTSCbBWfSeMWTAGUUd7FXtdLSKFZYGgHRUaRR9YC/V/ooI2m9YilgzShzYFdsQSDMzVA1SoW2wGGeEvOhfM4YMinHDE+jfI7BVN5pjLFkdQnWwbnci4vmM6EjqyhADMqK7LbAFVJeZaHUqU1gnbpiVTtc8C4Icd0TBjaSYmSUAn2eUYVoO3dFZRnvwLSNcB8PHi4ZND8w36jXeayp/QtPDPZxZ7mr1V0nYdLpRLxkNl+FLsGUJ7VyKumOwG3A9yZF6c7LYe4Q6VeN2r8qC4unntsklYNECFwu7W/djEe5i5rPZJdAzQ8S+isZoZOCOrnpTSCvsJ3aG0cP4IobuWxnlN5pvIYt2rVbHzdA+jv8JWeU5nkZu/nVv9RrInluu0A83LGij/LjWwrLFnQYAufkPek3/lPIbziu/wWt3OACaaoExKVllaba2gU8W7rU0xwgNv5zZHvkVqgo5Ej8l5uZkvhcJiQrdzI5zKjeL4V4VWXsXuN3SV/pK9kj7koSaM97xzWcQYnM59+gpzdtWMFnQM8ySP8kJ8SpVV8WivbFnAGQ/RToy/Zpdv8J5n/2iENAWkNouZOQfbPNoKfF/Te+ksW1WG4SnL/0uxhmz/bGj7xA9NeDGb/Z/6bYopJpphgnJ/FDe92yEe8vb32vWezmjNZzHBLBcm0P0yUkJ7i52zSP0mrGMXpsJDbWZk6dG9gtc4HZLDd/IjNWIcoHuRBoU6fHzWXZZlolCjV6nIoFvHvqT//INbx2du9TyH4aCZp0CeKfgFNmFxLiyYZzJTky/EPiQMG7SVPZBZBtS9jD3a2zug44iaZ49JS/Wme3Pyc2Knjb/lagAkdcFhX6UMKDIpOUTMKbhO/zA78iJ8k7TFfezkRjRqN9tRkFL/mhZy4oUFLBfBIYEm1DrHAflfH9cFKNAMoe0TPuL4wSINv5/51+gCwVYQE+NSoobQQGfnUfdTo6fQuSS9SbE6l+MAgUCciJGi1jorSfJgupcJBiDIjfi00/TToJIOTCc8fD8znnRGWs3ksp7jyl23PJr1myjOR/IerGOsAlltrr/Z6PGo8PhWu8HHj9HOPMWAtXGEMBWseCdjIIWPd3Sujb4RfDZKGh2NuIGgi7n0JrzAOH2SjjC3kH7nMOLyTj3KLHA3xcsdxQ/XLG3k/S4yDd/FrAbv5HJcYXYol/DGX6AfcbN0cQst5vCyzVffn2S1jsIDbeMFxMsxx/Pi6fhV7PQ/2ctMcXnTjyGcbN8lewYsQort5t9UddMxt9vCeyt0a8DYDPnyRtx6FLUscT0+289boC3VgE14icqxrn+e13OH6fnMezZ281vu8p5MtgeKja+Ph/UW8jjdy7nFaI+842mge5DPyd/rJ9m4Hra7eevYzjEZW8FKuZqVzgjmG4kG+wFd4TNiYUg80+vrxvhkaWcIqydtm0nGiInqKH7MjHhNMz/RkBnvWJ07gmHvYhe9wOBwOh8PhcDgcDofD4XA4HA6Hw+FwOBwOh8PhcDgcDofD4XA4HA6Hw+FwOBwOh8PhcDgcDofD4XA4HA6Hw+FwOBwOh8PhcDgcDofD4XA4HA6Hw+FwOBwOh8PhcDgcDofD4XA4HA6HY/b5/+AVVQKNbJF3AAAAAElFTkSuQmCC'

def theme_selection():
  "Detect either dark or light theme and generate the layout"

  if darkdetect.isDark(): 
    PSG.theme("DarkBlack")
  else:
    PSG.theme("LightBlue6")
  layout = [
    [PSG.Text("NumPad-Keys", tooltip="Will send a key as from the numpad after the duration\nNumbers can be chained")],
    [PSG.Push(), PSG.Button("1", key="-NUM-1-", size=(3,1)), PSG.Button("2", key="-NUM-2-", size=(3,1)), PSG.Button("3", key="-NUM-3-", size=(3,1)), PSG.Push()],
    [PSG.Push(), PSG.Button("4", key="-NUM-4-", size=(3,1)), PSG.Button("5", key="-NUM-5-", size=(3,1)), PSG.Button("6", key="-NUM-6-", size=(3,1)), PSG.Push()],
    [PSG.Push(), PSG.Button("7", key="-NUM-7-", size=(3,1)), PSG.Button("8", key="-NUM-8-", size=(3,1)), PSG.Button("9", key="-NUM-9-", size=(3,1)), PSG.Push()],
    [PSG.Push(), PSG.Button("0", key="-NUM-0-", size=(3,1)), PSG.Push()],
    [PSG.Text("")],
    [PSG.HorizontalSeparator()],
    [PSG.Text("F-Keys", tooltip="Will enable to press all the function keys missing from the standard keyboard\nKey presses can be chained")],
    [PSG.Push(), PSG.Button("F13", key="-F13-", size=(5,1)), PSG.Push(), PSG.Button("F14", key="-F14-", size=(5,1)), PSG.Push(), PSG.Button("F15", key="-F15-", size=(5,1)), PSG.Push(), PSG.Button("F16", key="-F16-", size=(5,1)), PSG.Push()],
    [PSG.Push(), PSG.Button("F17", key="-F17-", size=(5,1)), PSG.Push(), PSG.Button("F18", key="-F18-", size=(5,1)), PSG.Push(), PSG.Button("F19", key="-F19-", size=(5,1)), PSG.Push(), PSG.Button("F20", key="-F20-", size=(5,1)), PSG.Push()],
    [PSG.Push(), PSG.Button("F21", key="-F21-", size=(5,1)), PSG.Push(), PSG.Button("F22", key="-F22-", size=(5,1)), PSG.Push(), PSG.Button("F23", key="-F23-", size=(5,1)), PSG.Push(), PSG.Button("F24", key="-F24-", size=(5,1)), PSG.Push()],
    [PSG.Text("")],
    [PSG.HorizontalSeparator()],
    [PSG.Text("Modifier-Keys", tooltip="Standard modifier keys on a toggle for easier use")],
    [PSG.Checkbox("CTRL", key="-CTRL-", change_submits=True), PSG.Push(), PSG.Checkbox("SHIFT", key="-SHIFT-", change_submits=True), PSG.Push(), PSG.Checkbox("ESC", key="-ESC-", change_submits=True), PSG.Push(), PSG.Checkbox("ALT", key="-ALT-", change_submits=True)],
    [PSG.Text("")],
    [PSG.HorizontalSeparator()],
    [PSG.Text("Settings")],
    [PSG.Text("Delay (Seconds): ", tooltip="Delay, after which, the button will be pressed"), PSG.Input("2", key="-DELAY-INPUT-", size=(5,1))],
    [PSG.Text("Duration (ms): ", tooltip="Duration, during which, the button will be pressed"), PSG.Input("50", key="-DURATION-INPUT-", size=(5,1), pad=((22,0), 0))],
    [PSG.Checkbox("Keep Tool On Top", key="-KEEP-ON-TOP-", change_submits=True, default=True)],
    [PSG.Text("")],
    [PSG.HorizontalSeparator()],
    [PSG.Text("Status: "), PSG.Text("IDLE", key="-STATUS-")]
  ]
  return layout

def key_press(key:str, delay:float, duration:float, window:PSG.Window):
  """Send a key press after the delay and for the duration selected.
  Window parameter is used to update the status indicator"""

  window["-STATUS-"].update(f"Sending {key} in {delay}s")
  sleep(delay)
  window["-STATUS-"].update(f"Pressing {key}")
  pg.keyDown(key)
  sleep(duration)
  pg.keyUp(key)
  window["-STATUS-"].update("IDLE")

def main():
  layout = theme_selection()
  
  window = PSG.Window(f"PyKeyExtender | by Piombacciaio", layout, icon=icon(), finalize=True, keep_on_top=True, location=(0,0))
  while 1: 
    events, values = window.read()
    if events == PSG.WIN_CLOSED: break
    #Update KeepOnTop
    if events == "-KEEP-ON-TOP-":
      if values["-KEEP-ON-TOP-"]:
        window.keep_on_top_set()
      else:
        window.keep_on_top_clear()
    #CTRL Hold
    if events == "-CTRL-":
      if values["-CTRL-"]:
        pg.keyDown("ctrl")
      else:
        pg.keyUp("ctrl")
    #SHIFT Hold
    if events == "-SHIFT-":
      if values["-SHIFT-"]:
        pg.keyDown("shift")
      else:
        pg.keyUp("shift")
    #DEL Hold
    if events == "-ESC-":
      if values["-ESC-"]:
        pg.keyDown("esc")
      else:
        pg.keyUp("esc")
    #ALT Hold
    if events == "-ALT-":
      if values["-ALT-"]:
        pg.keyDown("alt")
      else:
        pg.keyUp("alt")
    #Keys Handler
    if events in [f"-NUM-{x}-" for x in range(0, 10)] or events in [f"-F{x}-" for x in range(13, 25)]:
      delay = float(values["-DELAY-INPUT-"])
      duration= float(values["-DURATION-INPUT-"])/1000
      key = events.replace("-", "")
      Thread(target=key_press, args=(key, delay, duration, window)).start()

if __name__ == '__main__': main()
