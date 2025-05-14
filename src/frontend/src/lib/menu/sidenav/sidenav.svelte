<script lang="ts">
	import Navlink from './navlink.svelte';
	import NavLink from './navlink.svelte';
	
    import { base } from '$app/paths';
</script>

<!-- Sidenav Menu Start -->
<div class="sidenav-menu">
	<!-- Brand Logo -->
	<a href="index.html" class="logo">
		<span class="logo-light">
			<span class="logo-lg"><img src="{base}/assets/images/logo.png" alt="logo" /></span>
			<span class="logo-sm"><img src="{base}/assets/images/logo-sm.png" alt="small logo" /></span>
		</span>

		<span class="logo-dark">
			<span class="logo-lg"><img src="{base}/assets/images/logo-dark.png" alt="dark logo" /></span>
			<span class="logo-sm"><img src="{base}/assets/images/logo-sm.png" alt="small logo" /></span>
		</span>
	</a>

	<!-- Sidebar Hover Menu Toggle Button -->
	<button class="button-sm-hover">
		<i class="ri-circle-line align-middle"></i>
	</button>

	<!-- Full Sidebar Menu Close Button -->
	<button class="button-close-fullsidebar">
		<i class="ti ti-x align-middle"></i>
	</button>

	<div data-simplebar>
		<!--- Sidenav Menu -->
		<ul class="side-nav">
			<li class="side-nav-title">Tools</li>

			<Navlink title="Dashboard" href="./" icon="ti ti-home" />

			<Navlink title="Map" href="map" icon="ti ti-cloud-rain" />

			<li class="side-nav-title mt-2">About</li>

			<Navlink title="About ParentTracking" href="about" icon="ti ti-info-circle" />
		</ul>

		<div class="clearfix"></div>
	</div>
</div>
<!-- Sidenav Menu End -->
