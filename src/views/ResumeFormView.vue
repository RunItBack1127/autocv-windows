<template>
    <form @submit.prevent="onSubmit">
        <div class="skillsDashboardContainer">
            <header>
                <label for="skillsDashboardInput">Update Relevant Skills</label>
                <p>Add up to 6 technologies.</p>
            </header>
            <SkillsDashboard
                :skills="skills"
                :disabled="skills.length === 6"
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
                <input @click.self="setCompetency('Microservices')" :class="competencySelection === 'Microservices' ? 'current-selection' : ''" type="button" value="Microservices" />
                <input @click.self="setCompetency('Databases')" :class="competencySelection === 'Databases' ? 'current-selection' : ''" type="button" value="Databases" />
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
        setCompetency(competency: string) {
            this.competencySelection = competency;
            console.log(competency);
        },
        addSkill(skill: string) {
            if( !this.skills.includes(skill) ) {
                this.skills.push(skill);
            }
        },
        removeSkill(skill: String) {
            console.log("Removing");
            this.skills = this.skills.filter((sk) => {
                return sk !== skill
            });
        }
    },
    data() {
        return {
            skills: [],
            competencySelection: 'Microservices'
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