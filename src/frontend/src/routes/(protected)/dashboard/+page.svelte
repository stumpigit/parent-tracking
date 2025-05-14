<script lang="ts">
	import pageTitle from '$lib/page/pageTitle';
	import { Map, View } from 'ol';
	import { Tile as TileLayer, Vector as VectorLayer } from 'ol/layer';
	import WebGLTileLayer from 'ol/layer/WebGLTile';
	import { XYZ, GeoTIFF } from 'ol/source';
	import { defaults as defaultControls, ScaleLine } from 'ol/control';
	import { register } from 'ol/proj/proj4';
	import proj4 from 'proj4';
	import { onMount } from 'svelte';
	import type { CupertinoSettings } from 'cupertino-pane';
	import { CupertinoPane } from 'cupertino-pane';

	import '../../../../node_modules/ol/ol.css';
	import { getBottomLeft } from 'ol/extent';

	$pageTitle = 'Dashboard';

	import { PUBLIC_HAKESCH_API_PATH } from '$env/static/public';
</script>

<svelte:head>
	<title>{$pageTitle} | ParentTracking</title>
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
					<h3 class="card-title">Map</h3>
					<p class="card-text">
						Some quick example text to build on the card title and make up the bulk of the card's
						content. Some quick example text to build on the card title and make up.
					</p>
					<a href="map" class="btn btn-primary">Start</a>
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
