<template>
    <form @submit.prevent="onSubmit">
        <div class="skillsDashboardContainer">
            <header>
                <label for="skillsDashboardInput">Update Relevant Skills</label>
                <p>Add 7 relevant technologies.</p>
            </header>
            <SkillsDashboard
                :skills="skills"
                :disabled="skills.length === 7"
                @modify-skill="(payload) => {
                    if( payload.method === 'REMOVE' ) {
                        removeSkill(payload.skill);
                    }
                    else {
                        addSkill(payload.skill);
                    }
                }" />
        </div>
        <div className="competenciesToggleContainer">
            <h1>Select Competency</h1>
            <div className="competenciesToggleInner">
                <input @click.self="setCompetency('Microservices')" :class="competency === 'Microservices' ? 'current-selection' : ''" type="button" value="Microservices" />
                <input @click.self="setCompetency('Databases')" :class="competency === 'Databases' ? 'current-selection' : ''" type="button" value="Databases" />
            </div>
        </div>
        <SubmitResetMenu @reset-form-fields="resetFormFields" />
    </form>
</template>

<script lang="ts">
import SiteHeader from '@/components/SiteHeader.vue';
import { computed } from '@vue/reactivity';
import { defineComponent } from 'vue';
import { useStore } from 'vuex';
import axios from 'axios';
import SkillsDashboard from '../components/SkillsDashboard.vue';
import SubmitResetMenu from '../components/SubmitResetMenu.vue';

export default defineComponent({
    components: {
        SiteHeader,
        SkillsDashboard,
        SubmitResetMenu
    },
    setup() {
        const store = useStore();

        return {
            skills: computed(() => store.state.resume.relevantSkills),
            competency: computed(() => store.state.resume.competency),
            setCompetency: (competency: string) => store.state.resume.competency = competency,
            addSkill: (skill: string) => {
                if(!store.state.resume.relevantSkills.includes(skill)) {
                    store.state.resume.relevantSkills.push(skill);
                }
            },
            removeSkill: (skill: string) => {
                store.state.resume.relevantSkills = store.state.resume.relevantSkills.filter((sk) => {
                    return sk !== skill;
                });
            },
            onSubmit: (e: Event) => {
                e.preventDefault();
                store.state.showLoadingScreen = true;
                document.querySelector("body").style.overflow = "hidden";

                axios.get("http://localhost:5000/resume", {
                    params: {
                        competency: store.state.resume.competency,
                        relevantSkills: store.state.resume.relevantSkills.join(","),
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
                store.state.resume.relevantSkills = [];
                store.state.resume.competency = 'Microservices';
            }
        }
    }
});
</script>

<style lang="scss" scoped>
form {

    .skillsDashboardContainer {
        header {
            label {
                font-size: 2rem;
                font-weight: 700;
            }

            p {
                font-size: 1.25rem;
                font-weight: 300;
                margin: 5px 0 40px;
                opacity: 0.35;
            }
        }
    }

    .competenciesToggleContainer {
        margin-bottom: 100px;

        h1 {
            margin-bottom: 25px;
        }

        .competenciesToggleInner {
            width: 100%;
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 0 50px;
            
            input[type="button"] {
                font-size: 1.25rem;
                padding: 25px 0;
                border-radius: 10px;
                border: 1px solid #000;
                background: transparent;
                transition: opacity 200ms ease;
                opacity: 0.25;
            }

            input[type="button"].current-selection {
                opacity: 1.0;
            }
        }
    }
}
</style>