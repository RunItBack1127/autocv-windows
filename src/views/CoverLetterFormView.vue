<template>
    <form>
        <BasicFormInput title="Name of Role" />
        <BasicFormInput title="Company Name" />
        <div class="customRecruiterContainer">
            <label for="customRecruiterCheckbox">Use custom recruiter name?</label>
            <input :checked="useCustomRecruiterName" type="checkbox" />
        </div>
        <BasicFormInput title="Recruiter Name" />
    </form>
</template>

<script setup lang="ts">
import BasicFormInput from '@/components/BasicFormInput.vue';
import { defineComponent, ref } from 'vue';

const nameOfRole = ref("");
const companyName = ref("");
const recruiterName = ref("");
const useCustomRecruiterName = ref(false);
</script>

<style lang="scss" scoped>

</style>