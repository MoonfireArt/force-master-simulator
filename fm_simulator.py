import random
import csv


def RollCrit(Rate):
    CritRoll = random.random() 
    if CritRoll < Rate:
        Crit = 1
    else:
        Crit = 0
    return Crit

def LMBT3S1(AP):
    dmg = AP * 3.2
    return dmg 

def LMBT4S1(AP, Embers):
    dmg = AP * (3.2 + (Embers * .3))
    if Embers==5:
        dmg = dmg * (1 + 1.5) # bonus explosion damage. Tooltip is wrong, not 75% per ember. Bug verified on the Dojo
    return dmg

def LMBT5S1(AP, Embers):
    dmg = AP * (3.4 + (Embers * .3))
    if Embers == 5:
        dmg = dmg * (1 + 1.5) # bonus explosion damage. Tooltip is wrong, not 75% per ember. Bug verified on the Dojo
    return dmg

def LMBT3S2(AP, BurnTimer):
    dmg = AP * 3.2
    if BurnTimer > 0:
        dmg = dmg + (AP * 0.8)
    return dmg

def LMBT5S2(AP, BurnTimer):
    dmg = AP * 3.2
    if BurnTimer > 0:
        dmg = dmg + (AP * 1.8)
    return dmg

def RMBT4S1(AP):
    dmg = AP * 1.5
    return dmg

def RMBT3S2(AP):
    dmg = AP * 1.5
    return dmg

def ShortFuse(AP):
    dmg = AP * 10.0
    return dmg

def Inferno(AP, Embers):
    dmg = AP * (11.0 + (.3 * Embers))
    if Embers == 2:
        dmg = dmg * 1.75
    elif Embers == 3:
        dmg = dmg * 2.0
    elif Embers == 4:
        dmg = dmg * 2.25
    elif Embers == 5:
        dmg = dmg * 2.50
    else:
        dmg = dmg
    return dmg

def Impact(AP): # Calculated for use on 5 ember stacks only
    dmg = (AP * 2.5) * 2.5
    return dmg

def Dragonblaze(AP, BurnTimer):
    dmg = AP * 9.0
    if BurnTimer > 0:
        dmg = dmg + (AP * 2.0)
    return dmg

def FireFury(AP, BurnTimer):
    dmg = AP * 4.5
    if BurnTimer > 0:
        dmg = dmg + AP
    return dmg

def BlazingBeam(AP, BurnTimer):
    dmg = AP * 6.0
    if BurnTimer > 0:
        dmg = dmg + (AP * 4.0)
    return dmg

def DualDragons(AP):
    dmg = AP * 18
    return dmg

def Meteor(AP, BurnTimer):
    dmg = AP * 12.0
    if BurnTimer > 0:
        dmg = dmg + (AP * 6.0)
    return dmg

def main():

    """ Introduction and data gathering"""
    print("Welcome to the Force Master Damage Simulator", "\n")
    print("This simulator currently only supports the following Builds:", "\n")
    print("\t", "Burn Build", "\n")
    print("\t", "Auto-Detonate Build", "\n")
    print("If you are using Ice Build, you are bad and should feel bad", "\n")
    print("Please select your LMB skill", "\n")
    print("\t", "1. Tier 3 Stage 1", "\n")
    print("\t", "2. Tier 4 Stage 1", "\n")
    print("\t", "3. Tier 5 Stage 1", "\n")
    print("\t", "4. Tier 3 Stage 2", "\n")
    print("\t", "5. Tier 5 Stage 2", "\n")
    LMBraw = input("Enter your LMB Skill (1 - 5): ")
    print("Please select your RMB path", "\n")
    print("\t", "1. Left Hand Path (Chill Stacks)", "\n")
    print("\t", "2. Right Hand Path (Frost Orbits)", "\n")
    RMBraw = input("Enter your RMB Skill choice (1-2): ")
    APraw = input("Enter your current AP: ")
    CritRateraw = input("Enter your Critical Hit Rate (the %, not the amount of Crit): ")
    CrtiDmgraw = input("Enter your Critical Damage Multiplier (the %, not the amount of Crit Damage): ")
    MinutesRaw = input("Enter the number of minutes (whole numbers only) you want this simulation to run: ")
    IterRaw = input("How many consecutive simulations do you want to run (each will be recorded seperately): ")


    #convert all inputs to proper data types
    LMB = int(LMBraw)
    RMB = int(RMBraw)
    AP = int(APraw)
    CritRateStep = float(CritRateraw)
    CritRate = CritRateStep * .01
    CritDmgStep = float(CrtiDmgraw)
    CritDmg = CritDmgStep * .01
    Minutes = int(MinutesRaw)
    Iter = int(IterRaw)

    for a in range(0, Iter, 1):
        # initalize variables
        BurnTimer = 0
        FireOrbits = 0
        FrostOrbits = 0
        FireOrbitTimer = 0
        FrostOrbitTimer = 0
        InfernoCD = 0
        ShortFuseCD = 0
        MeteorCD = 0
        DualDragonsCD = 0
        EmberStacks = 0
        TotalDamage = 0

        # Start For Loop (until number of seconds is up)
        for i in range(0, (Minutes * 60), 1):
            LMBdmg = 0
            RMBdmg = 0
            CdDamage = 0
    
        # Process RMB for current Second using IF
            if RMB==1:
                RMBdmg = RMBT4S1(AP) # call fucntion
                Critical = RollCrit(CritRate) #Roll for crit
                if Critical==1:
                    RMBdmg = RMBdmg * CritDmg # If a crit, multiply damage
            else:
                RMBdmg = RMBT3S2(AP) # call fucntion
                Critical = RollCrit(CritRate) #Roll for crit
                if Critical==1:
                    RMBdmg = RMBdmg * CritDmg # If a crit, multiply damage
                    if FrostOrbits < 3:
                        FrostOrbits = FrostOrbits + 1
                    FrostOrbitTimer = 30
            #print("RMB: ", RMBdmg)


        # Process LMB for current second using IF
            if LMB==1:
                LMBdmg = LMBT3S1(AP) #call fucntion
                Critical = RollCrit(CritRate) #Roll for crit
                if Critical==1:
                    LMBdmg = LMBdmg * CritDmg # If a crit, multiply damage
                    if FireOrbits < 3:
                        FireOrbits = FireOrbits + 1
                    FireOrbitTimer = 30
                if EmberStacks < 5:
                    EmberStacks = EmberStacks + 1
                else:
                    Emberstacks = 5
            elif LMB==2:
                LMBdmg = LMBT4S1(AP, EmberStacks) #call fucntion
                Critical = RollCrit(CritRate) #Roll for crit
                if Critical==1:
                    LMBdmg = LMBdmg * CritDmg # If a crit, multiply damage
                    if FireOrbits < 3:
                        FireOrbits = FireOrbits + 1
                    FireOrbitTimer = 30
                if EmberStacks == 5:
                    EmberStacks = 0
                if EmberStacks < 5:
                    EmberStacks = EmberStacks + 1
                else:
                    Emberstacks = 5
            elif LMB==3:
                LMBdmg = LMBT5S1(AP, EmberStacks) #call fucntion
                Critical = RollCrit(CritRate) #Roll for crit
                if Critical==1:
                    LMBdmg = LMBdmg * CritDmg # If a crit, multiply damage
                    if FireOrbits < 3:
                        FireOrbits = FireOrbits + 1
                    FireOrbitTimer = 30
                    if EmberStacks < 5:
                        EmberStacks = EmberStacks + 1
                    else:
                        Emberstacks = 5
                if EmberStacks == 5:
                    EmberStacks = 0
                if EmberStacks < 5:
                    EmberStacks = EmberStacks + 1
                else:
                    Emberstacks = 5
            elif LMB==4:
                LMBdmg = LMBT3S2(AP, BurnTimer) #call fucntion
                Critical = RollCrit(CritRate) #Roll for crit
                if Critical==1:
                    LMBdmg = LMBdmg * CritDmg # If a crit, multiply damage
                if BurnTimer > 0:
                    if EmberStacks < 5:
                        EmberStacks = EmberStacks + 1
                    else:
                        Emberstacks = 5
                if EmberStacks < 5:
                    EmberStacks = EmberStacks + 1
                else:
                    Emberstacks = 5
            else:
                LMBdmg = LMBT5S2(AP, BurnTimer) #call fucntion
                Critical = RollCrit(CritRate) #Roll for crit
                if Critical==1:
                    LMBdmg = LMBdmg * CritDmg # If a crit, multiply damage
                if BurnTimer > 0:
                    if EmberStacks < 5:
                        EmberStacks = EmberStacks + 1
                    else:
                        Emberstacks = 5
                if EmberStacks < 5:
                    EmberStacks = EmberStacks + 1
                else:
                    Emberstacks = 5
            #print("  LMB: ", LMBdmg)



        # Process CD action for this second using nested IF's
            if BurnTimer <= 0: #Triggers if burn has run out. Tries to use C, then X, then 1, and finally 2
                if ShortFuseCD <=0:
                    CdDamage = ShortFuse(AP) #call function to calcuate damage
                    Critical = RollCrit(CritRate) #Roll for crit
                    if Critical==1:
                        CdDamage = CdDamage * CritDmg # If a crit, multiply damage
                    BurnTimer = 10 #Reset burn timer
                    ShortFuseCD = 30 #Reset Cooldown
                    if FireOrbits < 3:
                        FireOrbits = FireOrbits + 1
                    FireOrbitTimer = 30
                    #print("  Short Fuse: ", CdDamage)
                elif InfernoCD <= 0:
                    CdDamage = Inferno(AP, EmberStacks) # call function to calculate damage
                    Critical = RollCrit(CritRate) #Roll for crit
                    if Critical==1:
                        CdDamage = CdDamage * CritDmg # If a crit, multiply damage
                    BurnTimer = 6 # Reset Burn Timer
                    InfernoCD = 45 # Reset Cooldown
                    #print("  Inferno: ", CdDamage)
                elif EmberStacks == 5:
                    CdDamage = Impact(AP) # call function to calculate damage
                    Critical = RollCrit(CritRate) # Roll for crit
                    if Critical==1:
                        CdDamage = CdDamage * CritDmg # If a crit, multiply damage
                    BurnTimer = 6 # Reset Burn Timer
                    EmberStacks = 0 # Blow up ember stacks
                    #print("  Impact: ", CdDamage)
                elif FireOrbits == 3:
                    CdDamage = Dragonblaze(AP, BurnTimer)
                    Critical = RollCrit(CritRate) # Roll for crit
                    if Critical==1:
                        CdDamage = CdDamage * CritDmg # If a crit, multiply damage
                    FireOrbits = 0
                    FireOrbitTimer = 0
                    MeteorCD = MeteorCD - 3
                    #print("  Dragonblaze: ", CdDamage)
                elif FireOrbits < 3 and LMB > 3 and FrostOrbits == 3:
                    CdDamage = FireFury(AP, BurnTimer)
                    Critical = RollCrit(CritRate) # Roll for crit
                    if Critical==1:
                        CdDamage = CdDamage * CritDmg # If a crit, multiply damage
                    FireOrbits = 3
                    if EmberStacks < 3:
                        EmberStacks = EmberStacks + 3
                    else:
                        Emberstacks = 5
                    #print("  Fire Fury: ", CdDamage)
                else:
                    CdDamage = BlazingBeam(AP, BurnTimer)
                    Critical = RollCrit(CritRate) # Roll for crit
                    if Critical==1:
                        CdDamage = CdDamage * CritDmg # If a crit, multiply damage
                    if EmberStacks < 5:
                        EmberStacks = EmberStacks + 1
                    else:
                        Emberstacks = 5
                    #print("  Blazing Beam: ", CdDamage)
            else:
                if MeteorCD <= 0:
                    CdDamage = Meteor(AP, BurnTimer)
                    Critical = RollCrit(CritRate) # Roll for crit
                    if Critical==1:
                        CdDamage = CdDamage * CritDmg # If a crit, multiply damage
                    EmberStacks = 5
                    MeteorCD = 45
                    #print("  Meteor Storm: ", CdDamage)
                elif FireOrbits < 3 and LMB > 3 and FrostOrbits == 3:
                    CdDamage = FireFury(AP, BurnTimer)
                    Critical = RollCrit(CritRate) # Roll for crit
                    if Critical==1:
                        CdDamage = CdDamage * CritDmg # If a crit, multiply damage
                    FireOrbits = 3
                    if EmberStacks < 3:
                        EmberStacks = EmberStacks + 3
                    else:
                        Emberstacks = 5
                    #print("  Fire Fury: ", CdDamage)
                elif FireOrbits == 3 and FrostOrbits == 3:
                    CdDamage = DualDragons(AP)
                    Critical = RollCrit(CritRate) # Roll for crit
                    if Critical==1:
                        CdDamage = CdDamage * CritDmg # If a crit, multiply damage
                    EmberStacks = 5
                    FireOrbits = 0
                    FrostOrbits = 0
                    DualDragonsCD = 18
                    #print("  Dual Dragons: ", CdDamage)
                elif FireOrbits == 3:
                    CdDamage = Dragonblaze(AP, BurnTimer)
                    Critical = RollCrit(CritRate) # Roll for crit
                    if Critical==1:
                        CdDamage = CdDamage * CritDmg # If a crit, multiply damage
                    FireOrbits = 0
                    FireOrbitTimer = 0
                    MeteorCD = MeteorCD - 3
                    #print("  Dragonblaze: ", CdDamage)
                else:
                    CdDamage = BlazingBeam(AP, BurnTimer)
                    Critical = RollCrit(CritRate) # Roll for crit
                    if Critical==1:
                        CdDamage = CdDamage * CritDmg # If a crit, multiply damage
                    if EmberStacks < 5:
                        EmberStacks = EmberStacks + 1
                    else:
                        Emberstacks = 5
                    #print("  Blazing Beam: ", CdDamage)
            
            #print("  Burn Timer: ", BurnTimer, "  Fire Orbits: ", FireOrbits, "  Frost Orbits: ", FrostOrbits, "\n") 
            BurnTimer = BurnTimer - 1
            FireOrbitTimer = FireOrbitTimer - 1
            if FireOrbitTimer <= 0:
                FireOrbits = 0
            FrostOrbitTimer = FrostOrbitTimer - 1
            if FrostOrbitTimer <= 0:
                FrostOrbits = 0
            InfernoCD = InfernoCD - 1
            ShortFuseCD = ShortFuseCD - 1
            MeteorCD = MeteorCD - 1
            DualDragonsCD = DualDragonsCD -1
            
            TotalDamage = TotalDamage + LMBdmg + RMBdmg + CdDamage

        #print("Your total elapsed time is ", Minutes, " minutes.")
        DPS = TotalDamage / (Minutes * 60)
        #print("Your total damage dealt was: ", TotalDamage)
        #print("Your average DPS was: ", DPS)
        output_file = open('SimResults.csv', 'a', newline='') # code to write output to a cs file for convenience
        data = csv.writer(output_file)
        data.writerow([LMB, RMB, AP, CritRateStep, CritDmg, Minutes, TotalDamage, DPS])
        del data
        output_file.close()
        del output_file
        

    Continue = input("Would you like to run another simulation (Y/N): ")
    if Continue == "Y" or Continue == "y":
        main()
    else:
        return 0

if __name__ == "__main__": main()


