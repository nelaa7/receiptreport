"use strict";
var KTSigninGeneral = function () {
    var e, t, i;
    return {
        init: function () {
            e = document.querySelector("#kt_sign_in_form"),
            t = document.querySelector("#kt_sign_in_submit"),
            i = FormValidation.formValidation(e, {
                fields: {
                    nik: { // Mengganti 'email' dengan 'nik'
                        validators: {
                            notEmpty: {
                                message: "NIK is required"
                            }
                        }
                    },
                    password: {
                        validators: {
                            notEmpty: {
                                message: "The password is required"
                            }
                        }
                    }
                },
                plugins: {
                    trigger: new FormValidation.plugins.Trigger,
                    bootstrap: new FormValidation.plugins.Bootstrap5({
                        rowSelector: ".fv-row",
                        eleInvalidClass: "",
                        eleValidClass: ""
                    })
                }
            }),

            t.addEventListener("click", function (n) {
                n.preventDefault();

                // Validasi form
                i.validate().then(function (result) {
                    if (result === "Valid") {
                        t.setAttribute("data-kt-indicator", "on");
                        t.disabled = !0;

                        const formData = new FormData(e); // Ambil data form

                        // Kirim permintaan AJAX
                        fetch(e.action, {
                            method: 'POST',
                            body: formData,
                            headers: {
                                'X-CSRFToken': e.querySelector('[name=csrfmiddlewaretoken]').value
                            }
                        })
                        .then(response => {
                            return response.json(); // Mengharapkan respons JSON
                        })
                        .then(data => {
                            if (data.success) {
                                Swal.fire({
                                    text: "You have successfully logged in!",
                                    icon: "success",
                                    buttonsStyling: !1,
                                    confirmButtonText: "Ok, got it!",
                                    customClass: {
                                        confirmButton: "btn btn-primary"
                                    }
                                }).then(function (t) {
                                    if (t.isConfirmed) {
                                        // Redirect to dashboard
                                        window.location.href = e.getAttribute("data-kt-redirect-url");
                                    }
                                });
                            } else {
                                Swal.fire({
                                    text: data.error || "Sorry, looks like there are some errors detected, please try again.",
                                    icon: "error",
                                    buttonsStyling: !1,
                                    confirmButtonText: "Ok, got it!",
                                    customClass: {
                                        confirmButton: "btn btn-primary"
                                    }
                                });
                            }
                        })
                        .catch(error => {
                            console.error('Error:', error);
                            Swal.fire({
                                text: "An unexpected error occurred. Please try again.",
                                icon: "error",
                                buttonsStyling: !1,
                                confirmButtonText: "Ok, got it!",
                                customClass: {
                                    confirmButton: "btn btn-primary"
                                }
                            });
                        })
                        .finally(() => {
                            t.removeAttribute("data-kt-indicator");
                            t.disabled = false;
                        });
                    } else {
                        Swal.fire({
                            text: "Sorry, looks like there are some errors detected, please try again.",
                            icon: "error",
                            buttonsStyling: !1,
                            confirmButtonText: "Ok, got it!",
                            customClass: {
                                confirmButton: "btn btn-primary"
                            }
                        });
                    }
                });
            });
        }
    }
}();
KTUtil.onDOMContentLoaded(function () {
    KTSigninGeneral.init();
});
