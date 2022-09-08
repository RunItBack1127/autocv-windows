<template>
    <form @submit.prevent="onSubmit">
        <BasicFormInput title="Name of Role" subText="Software Engineer" v-model="nameOfRole" />
        <BasicFormInput title="Company Name" subText="Cruise, LLC" v-model="companyName" />
        <div class="customRecruiterContainer">
            <label for="customRecruiterCheckbox">Use custom recruiter name?</label>
            <input tabindex="-1" type="checkbox" v-model="useCustomRecruiterName" />
        </div>
        <BasicFormInput
            title="Recruiter Name"
            subText="Bryan Danielson"
            v-model="recruiterName"
            :disabled="!useCustomRecruiterName" />
        <SubmitResetMenu
            :disabled="nameOfRole === '' || companyName === '' || (useCustomRecruiterName && recruiterName === '')"
            @reset-form-fields="resetFormFields" />
    </form>
</template>

<script lang="ts">
import BasicFormInput from '@/components/BasicFormInput.vue';
import SubmitResetMenu from '../components/SubmitResetMenu.vue';
import { defineComponent } from 'vue';
import { useStore } from 'vuex';
import axios from 'axios';

export default defineComponent({
    components: {
        BasicFormInput,
        SubmitResetMenu
    },
    data() {
        const store = useStore();

        return {
            nameOfRole: store.state.coverLetter.nameOfRole,
            companyName: store.state.coverLetter.companyName,
            recruiterName: store.state.coverLetter.recruiterName,
            useCustomRecruiterName: store.state.coverLetter.useCustomRecruiterName,
            persistState: () => {
                store.state.coverLetter.nameOfRole = this.nameOfRole;
                store.state.coverLetter.companyName = this.companyName;
                store.state.coverLetter.recruiterName = this.recruiterName;
                store.state.coverLetter.useCustomRecruiterName = this.useCustomRecruiterName;
            },
            onSubmit: (e: Event) => {
                e.preventDefault();
                store.state.showLoadingScreen = true;
                document.querySelector("body").style.overflow = "hidden";

                axios.get("http://localhost:5000/cv", {
                    params: {
                        recruiterName: this.recruiterName === "" ? 'Corporate Recruiter' : this.recruiterName,
                        companyName: this.companyName,
                        nameOfRole: this.nameOfRole,
                        applicantRole: store.state.settings.applicantRole
                    }
                }).then((response) => {
                    window.open(response.data.pdf);
                }).catch((e) => {
                    console.error(e);
                }).finally(() => {
                    store.state.showLoadingScreen = false;
                    document.querySelector("body").style.overflow = "";
                });
            },
            resetFormFields: () => {
                this.nameOfRole = "";
                this.companyName = "";
                this.recruiterName = "";
                this.useCustomRecruiterName = false;
            }
        }
    },
    beforeRouteLeave() {
        this.persistState();
    }
})
</script>

<style lang="scss" scoped>
form {

    .customRecruiterContainer {
        display: flex;
        justify-content: flex-end;
        align-items: center;
        width: 100%;

        label {
            font-size: 1.1rem;
            font-weight: 300;
            margin-right: 15px;
            opacity: 0.9;
        }
    }
}
</style>