const { createApp } = Vue;

createApp({
    data() {
        return {
            username: "",
            password: "",
            submitted: false,
            submittedName: "",
            message: "",
            isHidden: true
        };
    },

    mounted() {
        this.showMessage();
    },

    methods: {
        submitForm() {
            this.submittedName = this.username;
            this.submitted = true;
            this.$refs.loginForm.reset();
            this.username = "";
            this.password = "";
        },
        
        async showMessage() {
            const response = await fetch("/api/hello");
            const result = await response.json();
            this.message = result.message;
            
        }
    }
}).mount("#app");

