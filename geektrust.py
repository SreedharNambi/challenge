import sys
class WaterBill:
    def __init__(self,type_of_flat,ratio,addl_guest):
        self.type_of_flat=type_of_flat
        self.ratio=ratio
        self.addl_guest=addl_guest
    def BillAndWaterConsumed(self):
        if self.type_of_flat==2:
            water_alloted=900
        else:
            water_alloted=1500
        #if ratio='1:2' corporation share(a) = 1 and borewater share(b) = 2 
        a=int(self.ratio[0])
        b=int(self.ratio[2])
        corporation_water_share=water_alloted*(a/(a+b))
        borewell_water_share=water_alloted*(b/(a+b))
        corporation_water_bill=corporation_water_share*1 
        borewell_water_bill=borewell_water_share*1.5 
        total_individual_bill=corporation_water_bill+borewell_water_bill
        total_water_for_guest=300*(self.addl_guest)  #300L per guest per month
        
        #Tanker Water - Slab rate:
            # 0 to 500L - Rs. 2 per litre
            # 501L to 1500L - Rs. 3 per litre
            # 1501 to 3000L - Rs. 5 per litre
            # 3001L+ - Rs. 8 per litre
            
            #Below s1,s2,s3 and s4 are water division based on slab rate
            
        #Calculation the water bill for tanker water used by guests
        if total_water_for_guest<500:
            guest_water_bill=total_water_for_guest*2
        elif total_water_for_guest>=500 and total_water_for_guest<=1500:
            s1=500 
            s2=total_water_for_guest-500
            guest_water_bill=s1*2 + s2*3 
        elif total_water_for_guest>1500 and total_water_for_guest<=3000:
            s1=500
            s2=1000
            s3=total_water_for_guest-s1-s2
            guest_water_bill=s1*2 + s2*3 +s3*5
        else:
            s1=500
            s2=1000
            s3=1500
            s4=total_water_for_guest-s1-s2-s3
            guest_water_bill=s1*2 + s2*3 +s3*5+s4*8
        total_water_consumed = int(water_alloted+total_water_for_guest)
        total_bill_generated = int(total_individual_bill+guest_water_bill)
        print('{} {}'.format(total_water_consumed,total_bill_generated))
def main():
    input_file = sys.argv[1]
    # sys.argv[1] should give the absolute path to the input file
    # parse the file and process the command
    # print the output

if __name__ == "__main__":
    main()
         
N=input().split()
if N[0]=='ALLOT_WATER':
    type_of_flat=int(N[1])
    ratio=N[2]
input_con=[0,0]
addl_guest=0
while len(input_con)>1:
    input_con=input().split()
    if len(input_con)>1 and input_con[0]=='ADD_GUESTS':
        addl_guest+=int(input_con[1])
User_Details=WaterBill(type_of_flat,ratio,addl_guest)
User_Details.BillAndWaterConsumed()