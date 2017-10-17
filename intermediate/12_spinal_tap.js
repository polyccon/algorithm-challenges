//SPINAL TAP CASE
// Convert a string to spinal case. Spinal case is all-lowercase-words-joined-by-dashes.

function spinalCase(string) {

   return string.replace(/[^<]/, function myFunction(x){return x.toUpperCase();}).replace(/([A-Z])/g, '-$1').replace(/(\s)/g, '-').replace(/[^<]/, '').replace(/--/g, '-').replace(/_/g, '').toLowerCase();

}
spinalCase("This Is Spinal Tap"); //should return "this-is-spinal-tap".
spinalCase("thisIsSpinalTap"); //should return "this-is-spinal-tap".
spinalCase("The_Andy_Griffith_Show"); //should return "the-andy-griffith-show".
spinalCase("Teletubbies say Eh-oh"); //should return "teletubbies-say-eh-oh".
spinalCase("AllThe-small Things"); //should return "all-the-small-things".
