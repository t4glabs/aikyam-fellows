// Copyright (c) 2023, JinsoRaj and contributors
// For license information, please see license.txt
let create_challenge_url = frm => {
	let challenge_name = frm.doc.challenge_name;
	let challengeUrl = challenge_name.split(' ').join('_');
	frm.set_value("challenge_url", challengeUrl);
	frm.refresh_field("challenge_url");
}

frappe.ui.form.on('Challenge', {
	// refresh: function(frm) {
		challenge_name: (frm) =>{
			create_challenge_url(frm);
		}

	// }
});
