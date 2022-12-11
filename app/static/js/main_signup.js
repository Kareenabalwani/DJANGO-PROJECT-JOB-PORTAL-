function signup(){
      
  document.getElementById("connexion").classList.add('remove-section');
  document.getElementById("enregistrer").classList.remove('active-section');
  document.getElementById("btn-enregistrer").classList.remove("active");
  document.getElementById("btn-connexion").classList.add("active");
}
function signin(){
    
    document.getElementById("connexion").classList.remove('remove-section');
    document.getElementById("enregistrer").classList.add('active-section');
    document.getElementById("btn-enregistrer").classList.add("active");
    document.getElementById("btn-connexion").classList.remove("active");
}