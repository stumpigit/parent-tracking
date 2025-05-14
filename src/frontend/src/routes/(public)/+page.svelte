<script lang="ts">
	import { onMount } from 'svelte';
	import pageTitle from '$lib/page/pageTitle';

	$pageTitle = 'Dashboard';
</script>

<svelte:head>
	<title>{$pageTitle} | Parent-Tracking</title>
</svelte:head>

<div class="page-container">
	<div class="row row-cols-xxl-1 row-cols-md-1 row-cols-1">
		<div class="col">
			<div class="card d-block">
				<div class="card-body">
					<h1 class="card-title">Welcome to Parent-Tracking</h1>
					<p class="card-text">
						Welcome to the worlwide first parent tracking service. 
					</p>
				</div>
				<!-- end card-body-->
			</div>
			<!-- end card-->
		</div>
		<!-- end col -->
	</div>
	<!-- end row -->

	<div class="row">
		<div class="col-sm-6 col-lg-3">
			<!-- Simple card -->
			<div class="card d-block">
				<img
					class="card-img-top"
					src="assets/images/tools/precipitation.png"
					alt="Precipitation Tool"
				/>
				<div class="card-body">
					<h3 class="card-title">MyTracker</h3>
					<p class="card-text">
						Some quick example text to build on the card title and make up the bulk of the card's
						content. Some quick example text to build on the card title and make up.
					</p>
					<a href="precipitation.html" class="btn btn-primary">Start</a>
				</div>
				<!-- end card-body-->
			</div>
			<!-- end card-->
		</div>
		<!-- end col -->

	</div>
	<!-- end row -->
</div>
<!-- container -->
