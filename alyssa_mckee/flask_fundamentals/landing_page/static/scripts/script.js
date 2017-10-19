$(document).ready(function(){
	var isHidden = true;
	
	$(document).on("click", function(){
		if(isHidden){
			// reveal the ninja
			$("body").css({"background": "white", "color": "black"})
			isHidden = false
		}
		else{
			//hide the ninja
			$("body").css({"background": "black", "color": "white"})
			isHidden = true
		}
		
	})
})