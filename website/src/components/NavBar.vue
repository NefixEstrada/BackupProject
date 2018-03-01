<template>
  <b-navbar type="dark" variant="dark" toggleable>
    <b-navbar-brand to="/">Backup Project</b-navbar-brand>
    <b-navbar-toggle target="nav_dropdown_collapse"></b-navbar-toggle>
    <b-collapse is-nav id="nav_dropdown_collapse">
      <b-navbar-nav>
        <b-nav-item to="/about">About</b-nav-item>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</template>

<script>
export default {
  name: 'navBar'
}
</script>
