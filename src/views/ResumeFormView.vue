<template>
    <form @submit.prevent="onSubmit">
        <div class="skillsDashboardContainer">
            <header>
                <label for="skillsDashboardInput"></label>
                <p>Choose up to 6.</p>
            </header>
            <SkillsDashboard @add-skill="(skill: string) => addSkill(skill)" />
        </div>
        <div className="competenciesToggleContainer">
            <h1>Select Competency</h1>
            <div className="competenciesToggleInner">
                <input type="button" value="Microservices" />
                <input type="button" value="Databases" />
            </div>
        </div>
        <SubmitResetMenu />
    </form>
</template>

<script lang="ts">
import SiteHeader from '@/components/SiteHeader.vue';
import { defineComponent } from 'vue';
import SkillsDashboard from '../components/SkillsDashboard.vue';
import SubmitResetMenu from '../components/SubmitResetMenu.vue';

export default defineComponent({
    components: {
    SiteHeader,
    SkillsDashboard,
    SubmitResetMenu
},
    methods: {
        onSubmit(e: Event) {
            e.preventDefault();
            console.log("Submitted from resume form view");
        },
        addSkill(skill: string) {

        }
    },
    data() {
        return {
            skills: []
        }
    }
});
</script>

<style lang="scss" scoped>

</style>