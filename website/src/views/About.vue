<template>
  <!-- TODO: Add an about page -->
  <div id="about">
    <h1>About</h1>

    <p>Backup Project is a project that I've been doing in my free time. The goal of this project is to make a simple interface to create backups and automatizate them. You'll not have more exuses for having bad backups! The project uses <a href="https://www.borgbackup.org/">Borg Backup</a> for creating the backups. It has basically two parts:</p>

    <ul>
      <li>The front-end</li>
      <li>The back-end</li>
    </ul>

    <br>

    <h3>Front End</h3>
    <p>The front end is made with Vue. It uses other libraries too:</p>
    <ul>
      <li><a href="https://vuejs.org/">Vue</a></li>
      <li><a href="https://router.vuejs.org/">Vue Router</a></li>
      <li><a href="https://github.com/axios/axios">Axios</a></li>
      <li><a href="https://bootstrap-vue.js.org/">Bootstrap + Vue</a></li>
      <li><a href="https://jquery.com/">JQuery</a></li>
      <li><a href="https://github.com/xaksis/vue-good-table">Vue Good Tables</a></li>
      <li><a href="https://github.com/FortAwesome/vue-fontawesome">Vue Font Awesome</a></li>
    </ul>

    <br>

    <h3>Back End</h3>
    <p>The back end is made with Flask. It also uses other libraries too:</p>
    <ul>
      <li><a href="http://flask.pocoo.org/">Flask</a></li>
      <li><a href="https://flask-restful.readthedocs.io">Flask RESTful</a></li>
      <li><a href="https://github.com/CoryDolphin/flask-cors">Flask CORS</a></li>
    </ul>

    <br>

    <p>Made by <a href="https://github.com/NefixEstrada">Néfix Estrada</a></p>
    <p>Huge, huge thanks to <a href="https://sourceforge.net/u/apianti">apianti</a>, he helped me a lot with some hard functions!</p>
  </div>
</template>

<style lang="sass">
#about
  margin:
    top: 50px
</style>
