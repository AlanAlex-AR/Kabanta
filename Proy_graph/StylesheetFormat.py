Stylesheet = """

#Charge_pushButton,#DEFIB_pushButton, #Shock_pushButton, #UpEnergySelect_pushButton,#DownEnergySelect_pushButton, 
#UPO_pushButton, #DPO_pushButton,#UPR_pushButton,#DPR_pushButton
{
    color: black; 
    background-color: lightgray; 
    border-width: 1px; 
    border-radius: 12px; 
    border-color: black; 
    padding: 5px; 
    font: bold 18px; 
    }

#DEA_pushButton, #SYNC_pushButton, #DISCHARGE_pushButton
{
    color: black; 
    background-color: lightgray; 
    border-width: 1px; 
    border-radius: 8px; 
    border-color: black; 
    padding: 5px; 
    font: bold 14px; 

}
#confirmMenu_pushButton, #returnMenu_pushButton, #CPRMenu_pushButton, #sizeMenu_pushButton, #LEADMenu_pushButton, #paniMenu_pushButton
{
    color: white; 
    background-color: rgb(84,84,84);  
    border-width: 1px; 
    border-radius: 15px; 
    border-color: rgb(84,84,84); 
    padding: 5px; 
    font: bold 15px; 
}

#paniMenu_pushButton, #sizeMenu_pushButton
{
    color: white; 
    background-color: rgb(84,84,84);  
    border-width: 1px; 
    border-radius: 15px; 
    border-color: rgb(84,84,84); 
    padding: 5px; 
    font: 15px; 
}

 #alarmMenu_pushButton
{
    color: white; 
    background-color: rgb(84,84,84);  
    border-width: 1px; 
    border-radius: 15px; 
    border-color: rgb(84,84,84); 
    padding: 5px; 
    font:  15px; 
}

#energySelectLabel_pushButton {
    color: white; 
    background-color: rgb(254,22,27);  
    border-width: 0px; 
    border-radius: 8px; 
    border-color: rgb(254,22,27); 
    padding: 5px; 
    font: bold 13px; 
}

#pacerLabel_pushButton
{
    color: white; 
    background-color: rgb(0,127,55);  
    border-width: 1px; 
    border-radius: 8px; 
    border-color: rgb(0,127,55); 
    padding: 5px; 
    font: bold 15px; 

}
#PPMLabel_pushButton, #mALabel_pushButton
{
    color: white; 
    background-color: rgb(0,127,55);  
    border-width: 0px; 
    border-radius: 3px; 
    border-color: rgb(0,127,55); 
    padding: 4px; 
    font: bold 14px; 
}

#pacerRate_Label, #pacerOutput_Label, #simulationTimeLabel_Label
{
    color: white;
    border: none;
    background: none;
    font: bold 18px; 
}

#version_Label
{
    color: rgb(34,34,34);
    border: none;
    background: none;
    font: bold 14px;
}

#simulationTimeValue_pushButton
{
    color: red;
    background-color: black;  
    border: 1px solid; 
    border-radius: 12px;
    border-color: black;
    font: 22px; 
}

#heartRateLabel_pushButton
{
    color: black; 
    background-color: rgb(126,217,87);  
    border-width: 0px; 
    border-radius: 10px; 
    font: bold 15px; 
}

#heartRateValue_Label
{
    color: rgb(126,217,87);  
    font: bold 40px; 
}

#heartRateUnidades_Label
{
    color: rgb(126,217,87);  
    font: 17px; 
}

#tempLabel_pushButton
{
    color: black; 
    background-color: rgb(140,82,255);  
    border-width: 0px; 
    border-radius: 10px; 
    font: bold 15px; 
}

#tempValue_Label
{
    color: rgb(140,82,255);  
    font: bold 40px; 
}

#tempUnidades_Label
{
    Color: rgb(140,82,255);  
    font: 17px; 
}

#SpO2Label_pushButton
{
    color: black; 
    background-color: rgb(134,234,233);  
    border-width: 0px; 
    border-radius: 10px; 
    font: bold 15px; 
}
#SpO2Value_Label
{
    color: rgb(134,234,233);  
    font: bold 40px; 

}
#SpO2Unidades_Label
{
    color: rgb(134,234,233);  
    font: 17px; 
}

#pressureLabel_pushButton
{
    color: black; 
    background-color: rgb(255,22,22);  
    border-width: 0px; 
    border-radius: 10px; 
    font: bold 15px; 
}

#pressureValue_Label
{
    color: rgb(255,22,22);  
    font: bold 40px; 
}

#pressureUnidades_Label
{
    color: rgb(255,22,22);  
    font: 17px; 
}
#FRLabel_pushButton
{
    color: black; 
    background-color: rgb(255,222,89);  
    border-width: 0px; 
    border-radius: 10px; 
    font: bold 15px; 
}

#FRValue_Label
{
    color: rgb(255,222,89);  
    font: bold 40px; 
}

#FRUnidades_Label
{
    color: rgb(255,222,89);  
    font: 17px; 
}

#CO2Label_pushButton
{
    color: black; 
    background-color: rgb(241,255,255);  
    border-width: 0px; 
    border-radius: 10px; 
    font: bold 15px; 
}

#CO2Value_Label
{
    color: rgb(241,255,255);  
    font: bold 40px; 
}

#CO2Unidades_Label
{
    color: rgb(241,255,255);  
    font: 17px; 
}
#play_RoundButton, #pause_RoundButton, #stop_RoundButton, #question_RoundButton, #config_pushButton
{
    color: black; 
    background-color: rgb(84,84,84);  
    border-width: 0px; 
    border-radius: 22px;
    font: bold 8px; 
}

#OnOff_RoundButton
{
    background-color: rgb(41,41,41);  
    border: 2px solid; 
    border-radius: 26px;
    border-color: green;
}

#PPSQBackground_pushButton
{
    background-color: rgb(209,209,209);  
    border: 4px solid; 
    border-radius: 30px;
    border-color: rgb(50,50,50);
}

#CRPRateLabel_Label, #CRPTimeLabel_Label, #CRPFCTLabel_Label
{
    color: white;  
    font: 13px;
}
 

#CPRLabel_pushButton
{
    background-color: rgb(50,50,50);  
    border: 4px solid; 
    border-radius: 36px;
    border-color: rgb(221,224,232);
}

#CRPRateValue_Label, #CRPFCTValue_Label
{
    color: rgb(126,217,87);  
    font: bold 19px;
}

#CRPTimeValue_Label
{
    color: rgb(254,22,27);  
    font: bold 19px;
}

#pacemakerLabel_pushButton
{
    color: white;
    background-color: rgb(0,127,55);  
    border: 4px solid; 
    border-radius: 36px;
    border-color: white;
}

#defibLabel_pushButton
{
    color: white;
    background-color: rgb(254,22,27);  
    border: 4px solid; 
    border-radius: 36px;
    border-color: white;
    font: bold 34px;
}

#pacerLabelText_Label
{
    color: white;
    font: bold 34px;
}
#pacerValuemA_Label, #pacerValueppm_Label
{
    color: white;
    font:  24px;
}
"""

PressedStylesheet = """

#DEFIB_pushButton
{
    color: black; 
    background-color: rgb(254,22,27); 
    border-width: 1px; 
    border-radius: 12px; 
    border-color: black; 
    padding: 5px; 
    font: bold 18px; 
}

#Charge_pushButton 
{
    color: black; 
    background-color: rgb(255,204,0); 
    border-width: 1px; 
    border-radius: 12px; 
    border-color: black; 
    padding: 5px; 
    font: bold 18px; 
}
#Shock_pushButton
{
    color: black; 
    background-color: rgb(254,22,27); 
    border-width: 1px; 
    border-radius: 12px; 
    border-color: black; 
    padding: 5px; 
    font: bold 18px; 
}

#pacerLabel_pushButton
{
    color: rgb(255,204,0); 
    background-color: rgb(0,127,55);  
    border-width: 1px; 
    border-radius: 8px; 
    border-color: rgb(0,127,55); 
    padding: 5px; 
    font: bold 15px; 
}
#CPRMenu_pushButton
{
    color: rgb(255,204,0); 
    background-color: rgb(84,84,84);  
    border-width: 1px; 
    border-radius: 15px; 
    border-color: rgb(84,84,84); 
    padding: 5px; 
    font: bold 15px; 
    }

#DISCHARGE_pushButton
{
    color: black; 
    background-color: rgb(254,22,27); 
    border-width: 1px; 
    border-radius: 8px; 
    border-color: black; 
    padding: 5px; 
    font: bold 10px; 

}
"""