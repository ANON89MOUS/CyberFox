from colorama import Fore,Back,Style
import platform,os

OsName = platform.uname()[0]

def banner():
    if OsName == "Windows":
      os.system("cls")
    else:
      os.system("clear")
    print(Fore.LIGHTWHITE_EX+" (               )   (       *                (                     )       (")   
    print(Fore.LIGHTWHITE_EX+" )\ )  *   )  ( /(   )\ )  (  `           (   )\ )       (       ( /(       )\ )")  
    print(Fore.LIGHTWHITE_EX+"(()/(` )  /(  )\()) (()/(  )\))(        ( )\ (()/( (     )\      )\()) (   (()/( " )
    print(Fore.LIGHTWHITE_EX+"/(_))( )(_))((_)\   /(_)_)()\       ___  )((_) /(_)))\ ((((_)(  |((_)\  )\   /(_)) ")
    print(Fore.CYAN+" (_)) (_(_())   ((_) (_))  (_()((_)|___|((_)_ (_)) ((_) )\ _ )\ |_ ((_)((_) (_)) "  )
    print(Fore.CYAN+" CCCCCCC  YYYY   YYYY  BBBBBBBBBB  EEEEEEEE  RRRRRRRR    FFFFFFFF    OOOOOOO      XXXX   XXXX   ")
    print(Fore.CYAN+"CC          YYY YYY    BBB    BBB  EE        RRR    RRR  FFF       OOO      OOO     XXX XXX  ")
    print(Fore.CYAN+"C             YYY      BBBBBBBBBB  EEEEEEEE  RRR  RRR    FFFFFFFF  OOO      OOO        XX          ")
    print(Fore.CYAN+"CC            YY       BBB    BBB  EE        RRR RRR     FFF        OOO    OOO      XXX XXX        ")
    print(Fore.CYAN+" CCCCCCCC     Y        BBBBBBBBBB  EEEEEEEE  RRR   RRR   FFF          OOOOOO      XXXX   XXXX            ")
    print(Style.RESET_ALL)

banner()
