import Vue from 'vue';
import Router from 'vue-router';
import VulnerabilityCVE from '../components/VulnerabilityCVE.vue';
import VulnerabilityTeam from '../components/VulnerabilityTeam.vue';
import VulnerabilityContainer from '../components/VulnerabilityContainer.vue';
import Ping from '../components/Ping.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/cve',
      name: 'cve',
      component: VulnerabilityCVE,
    },
    {
      path: '/team',
      name: 'team',
      component: VulnerabilityTeam,
    },
    {
      path: '/container',
      name: 'container',
      component: VulnerabilityContainer,
    },
  //More routes were ommited due to the cost on my AWS server hosting this site
  //However this is where you add all other routes easily
  ],
});
