def WriteWCM (Path):
    PathToWCM=Path+".wcm"
    output_wcm=open(PathToWCM,"w")
    output_wcm.write('<block name="version">')
    
    output_wcm.write('<application name="WIPL-D Pro CAD" major="2024" minor="0" build="1"></application>')
    
    output_wcm.write('</block>')
    
    output_wcm.write('<block name="grid">')
    
    output_wcm.write('<setting name="resolution" xres="0.1" yres="0.1" zres="0.1" adaptive="yes"></setting>')
    
    output_wcm.write('</block>')
    
    output_wcm.write('<block name="settings">')
    
    output_wcm.write('<setting name="units" length="Meter" wire_radius="Meter" frequency="GHz" field="V/m" voltage="V"></setting>')
    
    output_wcm.write('<setting name="sewing" tolerance="0.001"></setting>')
    
    output_wcm.write('<setting name="SmallFeatureRemoval" size="1.0e-6" fraction_of="model"></setting>')
    
    output_wcm.write('<setting name="CroppingOptions" keep_solids="false" crop_selection="false" keep_dielectric="false" keep_metallic="false"></setting>')
    
    output_wcm.write('<setting name="FillHole" method="Create Patch" topology="Minimal" smooth_out="Prefer plane" smooth_in="Sharp"></setting>')
    
    output_wcm.write('<setting name="MeshMode" mode="auto" algorithm="planar"></setting>')
    
    output_wcm.write('<setting name="StlMesh" stlMeshSize="399.723" stlSurfAngleTol="30"></setting>')
    
    output_wcm.write('<setting name="PlanarMesh" planarMeshSize="1.7130997600000000e-01" planarSurfAngleTol="30" planarEdgeAngleTol="30" planarDefeaturingTolerance="0.0001" planarMergeTol="10" planarNarrowRatio="0.01" planarHybrid="false" planarMeshSizeCalculation="Default"></setting>')
    
    output_wcm.write('<setting name="Naming" Scheme="1"></setting>')
    
    output_wcm.write('<setting name="ReadWavesFromFile" read_waves_from_file="false" file_path=""></setting>')
    
    output_wcm.write('<setting name="WiplerMergeTolerance" MergeTolerance="0.00000001"></setting>')
    
    output_wcm.write('</block>')
    
    output_wcm.write('<block name="simulation">')
    
    output_wcm.write('<setting name="frequency" bands="1" fstart_1="StartFrequency" fstop_1="StopFrequency" nf_1="NumFrequencies" scale="lin" ref="0" maxpatch="2" large_patch_mesh_algo="advanced" PointsNumber_or_Step="Number"></setting>')
    
    output_wcm.write('<setting name="options" isAdvanced="false" ia="normal" ce="normal" apr="0" shadow="none" shadred="0" shaddis="0" phi="0" theta="0" mi="normal" mem="0" niter="1000" error="1e-3" reldis="2" group="3" prec="single" basis="modified(auto)" MinOrder="1" IncreaseOrderBy="0"></setting>')
    
    output_wcm.write('<validation name="option" AutoUnite="ask" ModDomainsAdjacent="ask" ModDomainsInvalid="ask"></validation>')
    
    output_wcm.write('<setting name="operation" mode="3"></setting>')
    
    output_wcm.write('</block>')
    
    output_wcm.write('<block name="cosite_simulation">')
    
    output_wcm.write('</block>')
    
    output_wcm.write('<block name="symmetry">')
    
    output_wcm.write('<plane name="0"></plane>')
    
    output_wcm.write('<green_function name="GreenFunction" type="Free Space" pbc_flag="false" pbc_x1="0" pbc_x2="0" pbc_y1="0" pbc_y2="0" pbc_z1="0" pbc_z2="0" pbc_domain="1" pbc_phi="0" pbc_theta="90" pbc_acceleration="0" pec_plane="Z" pmc_plane="Z" halfspace_N_sommerfield="1" halfspace_Er="1" halfspace_Ei="0" halfspace_Mr="1" halfspace_Mi="0"></green_function>')
    
    output_wcm.write('</block>')
    
    output_wcm.write('<block name="junctions">')
    
    output_wcm.write('<jun_type name="type" auto="false"></jun_type>')
    
    output_wcm.write('<junction name="1" radius="" vertex1="Wire1_Vertex1"></junction>')
    
    output_wcm.write('<junction name="2" radius="" vertex1="Wire1_Vertex2"></junction>')
    
    output_wcm.write('</block>')
    
    output_wcm.write('<block name="domains">')
    
    output_wcm.write('<domain name="1" material_name="vacuum" description="vacuum" type="General" NFflag="yes" Er="1" Ei="0" Mr="1" Mi="0" Sigma="0" Ro="0"></domain>')
    
    output_wcm.write('</block>')
    
    output_wcm.write('<block name="MaterialLibrarySort">')
    
    output_wcm.write('<Sort name="Sort" type="Name"></Sort>')
    
    output_wcm.write('</block>')
    
    output_wcm.write('<block name="generators">')
    
    output_wcm.write('<generator name="1" vreal="1" vimag="0" isFrill="Delta" radius1="0" radius2="0" index="1" asymmetry_images="{(1,0),(1,0),(1,0),(1,0),(1,0),(1,0),(1,0)}" asymmetry_image_flags="(0,0,0,0,0,0,0)" vertex="Wire1_Vertex1" edge="Wire1_Edge1"></generator>')
    
    output_wcm.write('</block>')
    
    output_wcm.write('<block name="CS">')
    
    output_wcm.write('<cs name="LCS1" originx="0" originy="0" originz="0" xAxisx="1" xAxisy="0" xAxisz="0" yAxisx="0" yAxisy="1" yAxisz="0" WCS="yes"></cs>')
    
    output_wcm.write('</block>')
    
    output_wcm.write('<block name="de-embedding">')
    
    output_wcm.write('<dep name="feed" plane="X" length="" sys_len=""></dep>')
    
    output_wcm.write('</block>')
    
    output_wcm.write('<block name="adjustable_symbols">')
    
    output_wcm.write('</block>')
    
    output_wcm.write('<block name="recommended_values">')
    
    output_wcm.write('<frequency name="frequency" bandwidth_percent="" bandwidth_symbol="" n_freq="" n_freq_symbol=""></frequency>')
    
    output_wcm.write('</block>')
    
    output_wcm.write('<block name="frequency_parallel_run">')
    
    output_wcm.write('<parallel_run name="parallel_run_parameters" active="false" n_parallel_runs="" reverse_order="false"></parallel_run>')
    
    output_wcm.write('</block>')
    
    output_wcm.write('<block name="sweep_parallel_run">')
    
    output_wcm.write('<parallel_run name="parallel_run_parameters" active="false" n_parallel_runs="" reverse_order="false"></parallel_run>')
    
    output_wcm.write('</block>')
    
    output_wcm.write('<block name="characteristic_modes">')
    
    output_wcm.write('<modes name="mode_number" n_modes="" n_total_modes=""></modes>')
    
    output_wcm.write('</block>')
    
    output_wcm.write('<block name="results">')
    
    output_wcm.write('<radiation name="rad" Nphi="73" phiStart="0" phiStop="360" Ntheta="73" thetaStart="-90" thetaStop="90" additionalRP="false" RPdistance="0" power_balance="false" gain_correction="false" YZS_correction="false" Calculate_RP="true"></radiation>')
    
    output_wcm.write('</block>')
    
    output_wcm.write('<block name="commands">')
    
    output_wcm.write('SetSymm "No symmetry" "No symmetry" "No symmetry" 1e-06 "release=2021_0_5"')
    
    output_wcm.write('DrawCylinder "Body1" (0,0,0) d/2 L/2-(0) "release=2025_0_1"')
    
    output_wcm.write('DrawCylinder "Body2" (0,0,0) d/2 gap-(0) "release=2025_0_1"')
    
    output_wcm.write('Subtract "Body3" {"Body2","Body1"} "release=2025_0_1"')
    
    output_wcm.write('MultipleCopy "Body3" 1 (0, 0, 0) (0, 0, 0) (1, 1, -1) "No" "release=2025_0_1"')
    
    output_wcm.write('DrawLine "Wire1" (0,0,-gap) (0,0,gap) d/50 1 "release=2025_0_1"')
    
    output_wcm.write('DrawJunction "1" "VertexList" {"Wire1_Vertex1"} 0 "release=2025_0_1"')
    
    output_wcm.write('DrawJunction "2" "VertexList" {"Wire1_Vertex2"} 0 "release=2025_0_1"')
    
    output_wcm.write('DrawGenerator "1" ("Wire1_Vertex1","Wire1_Vertex2") "Wire1_Edge1" (1, 0) "Delta" (0 0) {(1,0) , (1,0) , (1,0) , (1,0) , (1,0) , (1,0) , (1,0)} (0,0,0,0,0,0,0) "release=2025_0_1"')
    
    output_wcm.write('</block>')
    
    output_wcm.close()
