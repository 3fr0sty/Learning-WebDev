const { createApp } = Vue;

createApp({
    data() {
        return {
            username: "",
            password: "",
            message: ""
        };
    },

    methods: {
        async login() {
            const formData = new FormData();

            formData.append("username", this.username);
            formData.append("password", this.password);

            const response = await fetch("/login.html", {
                method: "POST",
                body: formData
            });

            const data = await response.json();

            this.message = data.message;

            if (data.success) {
                window.location.href = "index.html";
            }
        }
    }
}).mount("#loginApp");