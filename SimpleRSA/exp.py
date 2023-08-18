import gmpy2 as gp 
from Crypto.Util.number import * 
p=24724324630507415330944861660078769085865178656494256140070836181271808964994457686409910764936630391300708451701526900994412268365698217113884698394658886249353179639767806926527103624836198494439742123128823109527320850165486500517304731554371680236789357527395416607541627295126502440202040826686102479225702795427693781581584928770373613126894936500089282093366117940069743670997994742595407158340397268147325612840109162997306902492023078425623839297511182053658542877738887677835528624045235391227122453939459585542485427063193993069301141720316104612551340923656979591045138487394366671477460626997125944456537
c=510345661718450375632304764819724223824018609359964259503762283253350010161515190912152623604019093266967095847334388281390406831587663253164256543905694021952211220652820225527413861208452760215767828927039893435528572148282529198773772864255061213208279999011194952146362748485103032149806538140693537361755210176698895104708379400806511907719904867068865970241208806615061055047254026118016836750283966478103987375361826198930529462261013324904522014804502582865716441828895047550041401172127129749969507853355531197814919603963664646220505672302543085959372679395717892060245461464861507164276442140407308832537707450729432224150754603518526288767105682399190438680085925078051459448618725871249563011864525585870188123725554411655044152994826056900502298772802133526591794328224932405680583757307064395792317383571866619582974377344736930271554160701478385763426091091686496788999588340419226785217028504684542197970387916262126278955278523452903043316452825738030645100271595942652498852506660789605846309602343932245435421425673058238785509280366229754404949219663043627431437755087855502139890639468481922788973821783957766433857773771229298328019250652625289700950165414584983487319078090573179470893450632419467111117341472


e = 65537 
d = gp.invert(e,p-1)
print(long_to_bytes(gp.powmod(c,d,p))) 
# b'SYC{Just_a_s1mple_modular_equation}'
