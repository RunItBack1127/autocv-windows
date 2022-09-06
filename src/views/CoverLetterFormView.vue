<template>
    <form>
        <BasicFormInput title="Name of Role" placeholder="Software Engineer" v-model="nameOfRole" />
        <BasicFormInput title="Company Name" placeholder="Cruise, LLC" v-model="companyName" />
        <div class="customRecruiterContainer">
            <label for="customRecruiterCheckbox">Use custom recruiter name?</label>
            <input type="checkbox" v-model="useCustomRecruiterName" />
        </div>
        <BasicFormInput
            title="Recruiter Name"
            placeholder="Corporate Recruiter"
            v-model="recruiterName"
            :disabled="!useCustomRecruiterName" />
        <SubmitClearMenu />
    </form>
</template>

<script lang="ts">
import BasicFormInput from '@/components/BasicFormInput.vue';
import SubmitClearMenu from '../components/SubmitClearMenu.vue';
import { defineComponent } from 'vue';

export default defineComponent({
    components: {
    BasicFormInput,
    SubmitClearMenu
},
    data() {
        return {
            nameOfRole: '',
            companyName: '',
            recruiterName: '',
            useCustomRecruiterName: false
        }
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
            font-weight: 500;
            margin-right: 15px;
            opacity: 0.9;
        }
    }
}
</style>