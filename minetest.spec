#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : minetest
Version  : 0.4.15
Release  : 16
URL      : https://github.com/minetest/minetest/archive/0.4.15.tar.gz
Source0  : https://github.com/minetest/minetest/archive/0.4.15.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC-BY-SA-3.0 LGPL-2.1+ MIT
Requires: minetest-bin
Requires: minetest-data
Requires: minetest-doc
BuildRequires : bzip2-dev
BuildRequires : cmake
BuildRequires : curl-dev
BuildRequires : gmp-dev
BuildRequires : irrlicht-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libogg-dev
BuildRequires : libvorbis-dev
BuildRequires : mesa-dev
BuildRequires : ncurses-dev
BuildRequires : openal-soft-dev
BuildRequires : pkgconfig(libpng)
BuildRequires : pkgconfig(x11)
BuildRequires : sqlite-autoconf-dev
BuildRequires : zlib-dev

%description
Minetest
========
An InfiniMiner/Minecraft inspired game.
and contributors (see source file comments and the version control log)

%package bin
Summary: bin components for the minetest package.
Group: Binaries
Requires: minetest-data

%description bin
bin components for the minetest package.


%package data
Summary: data components for the minetest package.
Group: Data

%description data
data components for the minetest package.


%package doc
Summary: doc components for the minetest package.
Group: Documentation

%description doc
doc components for the minetest package.


%prep
%setup -q -n minetest-0.4.15

%build
export LANG=C
mkdir clr-build
pushd clr-build
cmake .. -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS:BOOL=ON -DLIB_INSTALL_DIR:PATH=%{_libdir} -DCMAKE_AR=/usr/bin/gcc-ar -DLIB_SUFFIX=64 -DCMAKE_RANLIB=/usr/bin/gcc-ranlib -DBUILD_CLIENT=1 -DBUILD_SERVER=1 -DENABLE_FREETYPE=1 -DBUILD_SHARED_LIBS=0
make VERBOSE=1  %{?_smp_mflags}
popd

%install
rm -rf %{buildroot}
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/minetest
/usr/bin/minetestserver

%files data
%defattr(-,root,root,-)
/usr/share/appdata/minetest.appdata.xml
/usr/share/applications/minetest.desktop
/usr/share/icons/hicolor/128x128/apps/minetest.png
/usr/share/icons/hicolor/scalable/apps/minetest.svg
/usr/share/minetest/builtin/async/init.lua
/usr/share/minetest/builtin/common/async_event.lua
/usr/share/minetest/builtin/common/filterlist.lua
/usr/share/minetest/builtin/common/misc_helpers.lua
/usr/share/minetest/builtin/common/serialize.lua
/usr/share/minetest/builtin/common/strict.lua
/usr/share/minetest/builtin/common/vector.lua
/usr/share/minetest/builtin/fstk/buttonbar.lua
/usr/share/minetest/builtin/fstk/dialog.lua
/usr/share/minetest/builtin/fstk/tabview.lua
/usr/share/minetest/builtin/fstk/ui.lua
/usr/share/minetest/builtin/game/auth.lua
/usr/share/minetest/builtin/game/chatcommands.lua
/usr/share/minetest/builtin/game/constants.lua
/usr/share/minetest/builtin/game/deprecated.lua
/usr/share/minetest/builtin/game/detached_inventory.lua
/usr/share/minetest/builtin/game/falling.lua
/usr/share/minetest/builtin/game/features.lua
/usr/share/minetest/builtin/game/forceloading.lua
/usr/share/minetest/builtin/game/init.lua
/usr/share/minetest/builtin/game/item.lua
/usr/share/minetest/builtin/game/item_entity.lua
/usr/share/minetest/builtin/game/misc.lua
/usr/share/minetest/builtin/game/privileges.lua
/usr/share/minetest/builtin/game/register.lua
/usr/share/minetest/builtin/game/statbars.lua
/usr/share/minetest/builtin/game/static_spawn.lua
/usr/share/minetest/builtin/game/voxelarea.lua
/usr/share/minetest/builtin/init.lua
/usr/share/minetest/builtin/mainmenu/common.lua
/usr/share/minetest/builtin/mainmenu/dlg_config_world.lua
/usr/share/minetest/builtin/mainmenu/dlg_create_world.lua
/usr/share/minetest/builtin/mainmenu/dlg_delete_mod.lua
/usr/share/minetest/builtin/mainmenu/dlg_delete_world.lua
/usr/share/minetest/builtin/mainmenu/dlg_rename_modpack.lua
/usr/share/minetest/builtin/mainmenu/dlg_settings_advanced.lua
/usr/share/minetest/builtin/mainmenu/gamemgr.lua
/usr/share/minetest/builtin/mainmenu/generate_from_settingtypes.lua
/usr/share/minetest/builtin/mainmenu/init.lua
/usr/share/minetest/builtin/mainmenu/init_simple.lua
/usr/share/minetest/builtin/mainmenu/modmgr.lua
/usr/share/minetest/builtin/mainmenu/store.lua
/usr/share/minetest/builtin/mainmenu/tab_credits.lua
/usr/share/minetest/builtin/mainmenu/tab_mods.lua
/usr/share/minetest/builtin/mainmenu/tab_multiplayer.lua
/usr/share/minetest/builtin/mainmenu/tab_server.lua
/usr/share/minetest/builtin/mainmenu/tab_settings.lua
/usr/share/minetest/builtin/mainmenu/tab_simple_main.lua
/usr/share/minetest/builtin/mainmenu/tab_singleplayer.lua
/usr/share/minetest/builtin/mainmenu/tab_texturepacks.lua
/usr/share/minetest/builtin/mainmenu/textures.lua
/usr/share/minetest/builtin/profiler/init.lua
/usr/share/minetest/builtin/profiler/instrumentation.lua
/usr/share/minetest/builtin/profiler/reporter.lua
/usr/share/minetest/builtin/profiler/sampling.lua
/usr/share/minetest/builtin/settingtypes.txt
/usr/share/minetest/client/serverlist/.gitignore
/usr/share/minetest/client/shaders/default_shader/opengl_fragment.glsl
/usr/share/minetest/client/shaders/default_shader/opengl_vertex.glsl
/usr/share/minetest/client/shaders/minimap_shader/opengl_fragment.glsl
/usr/share/minetest/client/shaders/minimap_shader/opengl_vertex.glsl
/usr/share/minetest/client/shaders/nodes_shader/opengl_fragment.glsl
/usr/share/minetest/client/shaders/nodes_shader/opengl_vertex.glsl
/usr/share/minetest/client/shaders/selection_shader/opengl_fragment.glsl
/usr/share/minetest/client/shaders/selection_shader/opengl_vertex.glsl
/usr/share/minetest/client/shaders/water_surface_shader/opengl_fragment.glsl
/usr/share/minetest/client/shaders/water_surface_shader/opengl_vertex.glsl
/usr/share/minetest/client/shaders/wielded_shader/opengl_fragment.glsl
/usr/share/minetest/client/shaders/wielded_shader/opengl_vertex.glsl
/usr/share/minetest/fonts/DroidSansFallbackFull.ttf
/usr/share/minetest/fonts/liberationmono.ttf
/usr/share/minetest/fonts/liberationsans.ttf
/usr/share/minetest/fonts/lucida_sans_10.xml
/usr/share/minetest/fonts/lucida_sans_100.png
/usr/share/minetest/fonts/lucida_sans_11.xml
/usr/share/minetest/fonts/lucida_sans_110.png
/usr/share/minetest/fonts/lucida_sans_12.xml
/usr/share/minetest/fonts/lucida_sans_120.png
/usr/share/minetest/fonts/lucida_sans_14.xml
/usr/share/minetest/fonts/lucida_sans_140.png
/usr/share/minetest/fonts/lucida_sans_16.xml
/usr/share/minetest/fonts/lucida_sans_160.png
/usr/share/minetest/fonts/lucida_sans_18.xml
/usr/share/minetest/fonts/lucida_sans_180.png
/usr/share/minetest/fonts/lucida_sans_20.xml
/usr/share/minetest/fonts/lucida_sans_200.png
/usr/share/minetest/fonts/lucida_sans_22.xml
/usr/share/minetest/fonts/lucida_sans_220.png
/usr/share/minetest/fonts/lucida_sans_24.xml
/usr/share/minetest/fonts/lucida_sans_240.png
/usr/share/minetest/fonts/lucida_sans_26.xml
/usr/share/minetest/fonts/lucida_sans_260.png
/usr/share/minetest/fonts/lucida_sans_28.xml
/usr/share/minetest/fonts/lucida_sans_280.png
/usr/share/minetest/fonts/lucida_sans_36.xml
/usr/share/minetest/fonts/lucida_sans_360.png
/usr/share/minetest/fonts/lucida_sans_4.xml
/usr/share/minetest/fonts/lucida_sans_40.png
/usr/share/minetest/fonts/lucida_sans_48.xml
/usr/share/minetest/fonts/lucida_sans_480.png
/usr/share/minetest/fonts/lucida_sans_56.xml
/usr/share/minetest/fonts/lucida_sans_560.png
/usr/share/minetest/fonts/lucida_sans_6.xml
/usr/share/minetest/fonts/lucida_sans_60.png
/usr/share/minetest/fonts/lucida_sans_8.xml
/usr/share/minetest/fonts/lucida_sans_80.png
/usr/share/minetest/fonts/lucida_sans_9.xml
/usr/share/minetest/fonts/lucida_sans_90.png
/usr/share/minetest/fonts/mono_dejavu_sans_10.xml
/usr/share/minetest/fonts/mono_dejavu_sans_100.png
/usr/share/minetest/fonts/mono_dejavu_sans_11.xml
/usr/share/minetest/fonts/mono_dejavu_sans_110.png
/usr/share/minetest/fonts/mono_dejavu_sans_12.xml
/usr/share/minetest/fonts/mono_dejavu_sans_120.png
/usr/share/minetest/fonts/mono_dejavu_sans_14.xml
/usr/share/minetest/fonts/mono_dejavu_sans_140.png
/usr/share/minetest/fonts/mono_dejavu_sans_16.xml
/usr/share/minetest/fonts/mono_dejavu_sans_160.png
/usr/share/minetest/fonts/mono_dejavu_sans_18.xml
/usr/share/minetest/fonts/mono_dejavu_sans_180.png
/usr/share/minetest/fonts/mono_dejavu_sans_20.xml
/usr/share/minetest/fonts/mono_dejavu_sans_200.png
/usr/share/minetest/fonts/mono_dejavu_sans_22.xml
/usr/share/minetest/fonts/mono_dejavu_sans_220.png
/usr/share/minetest/fonts/mono_dejavu_sans_24.xml
/usr/share/minetest/fonts/mono_dejavu_sans_240.png
/usr/share/minetest/fonts/mono_dejavu_sans_26.xml
/usr/share/minetest/fonts/mono_dejavu_sans_260.png
/usr/share/minetest/fonts/mono_dejavu_sans_28.xml
/usr/share/minetest/fonts/mono_dejavu_sans_280.png
/usr/share/minetest/fonts/mono_dejavu_sans_4.xml
/usr/share/minetest/fonts/mono_dejavu_sans_40.png
/usr/share/minetest/fonts/mono_dejavu_sans_6.xml
/usr/share/minetest/fonts/mono_dejavu_sans_60.png
/usr/share/minetest/fonts/mono_dejavu_sans_8.xml
/usr/share/minetest/fonts/mono_dejavu_sans_80.png
/usr/share/minetest/fonts/mono_dejavu_sans_9.xml
/usr/share/minetest/fonts/mono_dejavu_sans_90.png
/usr/share/minetest/games/minimal/game.conf
/usr/share/minetest/games/minimal/menu/background.png
/usr/share/minetest/games/minimal/menu/icon.png
/usr/share/minetest/games/minimal/mods/bucket/depends.txt
/usr/share/minetest/games/minimal/mods/bucket/init.lua
/usr/share/minetest/games/minimal/mods/bucket/textures/bucket.png
/usr/share/minetest/games/minimal/mods/bucket/textures/bucket_lava.png
/usr/share/minetest/games/minimal/mods/bucket/textures/bucket_water.png
/usr/share/minetest/games/minimal/mods/default/init.lua
/usr/share/minetest/games/minimal/mods/default/mapgen.lua
/usr/share/minetest/games/minimal/mods/default/sounds/default_grass_footstep.1.ogg
/usr/share/minetest/games/minimal/mods/default/textures/bubble.png
/usr/share/minetest/games/minimal/mods/default/textures/crack_anylength.png
/usr/share/minetest/games/minimal/mods/default/textures/default_apple.png
/usr/share/minetest/games/minimal/mods/default/textures/default_book.png
/usr/share/minetest/games/minimal/mods/default/textures/default_bookshelf.png
/usr/share/minetest/games/minimal/mods/default/textures/default_brick.png
/usr/share/minetest/games/minimal/mods/default/textures/default_cactus_side.png
/usr/share/minetest/games/minimal/mods/default/textures/default_cactus_top.png
/usr/share/minetest/games/minimal/mods/default/textures/default_chest_front.png
/usr/share/minetest/games/minimal/mods/default/textures/default_chest_lock.png
/usr/share/minetest/games/minimal/mods/default/textures/default_chest_side.png
/usr/share/minetest/games/minimal/mods/default/textures/default_chest_top.png
/usr/share/minetest/games/minimal/mods/default/textures/default_clay.png
/usr/share/minetest/games/minimal/mods/default/textures/default_clay_brick.png
/usr/share/minetest/games/minimal/mods/default/textures/default_clay_lump.png
/usr/share/minetest/games/minimal/mods/default/textures/default_cloud.png
/usr/share/minetest/games/minimal/mods/default/textures/default_coal_lump.png
/usr/share/minetest/games/minimal/mods/default/textures/default_cobble.png
/usr/share/minetest/games/minimal/mods/default/textures/default_dirt.png
/usr/share/minetest/games/minimal/mods/default/textures/default_fence.png
/usr/share/minetest/games/minimal/mods/default/textures/default_furnace_fire_bg.png
/usr/share/minetest/games/minimal/mods/default/textures/default_furnace_fire_fg.png
/usr/share/minetest/games/minimal/mods/default/textures/default_furnace_front.png
/usr/share/minetest/games/minimal/mods/default/textures/default_furnace_front_active.png
/usr/share/minetest/games/minimal/mods/default/textures/default_furnace_side.png
/usr/share/minetest/games/minimal/mods/default/textures/default_glass.png
/usr/share/minetest/games/minimal/mods/default/textures/default_grass.png
/usr/share/minetest/games/minimal/mods/default/textures/default_grass_footsteps.png
/usr/share/minetest/games/minimal/mods/default/textures/default_grass_side.png
/usr/share/minetest/games/minimal/mods/default/textures/default_gravel.png
/usr/share/minetest/games/minimal/mods/default/textures/default_iron_lump.png
/usr/share/minetest/games/minimal/mods/default/textures/default_junglegrass.png
/usr/share/minetest/games/minimal/mods/default/textures/default_ladder.png
/usr/share/minetest/games/minimal/mods/default/textures/default_lava.png
/usr/share/minetest/games/minimal/mods/default/textures/default_lava_flowing_animated.png
/usr/share/minetest/games/minimal/mods/default/textures/default_lava_source_animated.png
/usr/share/minetest/games/minimal/mods/default/textures/default_leaves.png
/usr/share/minetest/games/minimal/mods/default/textures/default_mese.png
/usr/share/minetest/games/minimal/mods/default/textures/default_mineral_coal.png
/usr/share/minetest/games/minimal/mods/default/textures/default_mineral_iron.png
/usr/share/minetest/games/minimal/mods/default/textures/default_mossycobble.png
/usr/share/minetest/games/minimal/mods/default/textures/default_nc_back.png
/usr/share/minetest/games/minimal/mods/default/textures/default_nc_front.png
/usr/share/minetest/games/minimal/mods/default/textures/default_nc_rb.png
/usr/share/minetest/games/minimal/mods/default/textures/default_nc_side.png
/usr/share/minetest/games/minimal/mods/default/textures/default_paper.png
/usr/share/minetest/games/minimal/mods/default/textures/default_papyrus.png
/usr/share/minetest/games/minimal/mods/default/textures/default_rail.png
/usr/share/minetest/games/minimal/mods/default/textures/default_rail_crossing.png
/usr/share/minetest/games/minimal/mods/default/textures/default_rail_curved.png
/usr/share/minetest/games/minimal/mods/default/textures/default_rail_t_junction.png
/usr/share/minetest/games/minimal/mods/default/textures/default_sand.png
/usr/share/minetest/games/minimal/mods/default/textures/default_sandstone.png
/usr/share/minetest/games/minimal/mods/default/textures/default_sapling.png
/usr/share/minetest/games/minimal/mods/default/textures/default_scorched_stuff.png
/usr/share/minetest/games/minimal/mods/default/textures/default_sign_wall.png
/usr/share/minetest/games/minimal/mods/default/textures/default_steel_block.png
/usr/share/minetest/games/minimal/mods/default/textures/default_steel_ingot.png
/usr/share/minetest/games/minimal/mods/default/textures/default_stick.png
/usr/share/minetest/games/minimal/mods/default/textures/default_stone.png
/usr/share/minetest/games/minimal/mods/default/textures/default_tnt_bottom.png
/usr/share/minetest/games/minimal/mods/default/textures/default_tnt_side.png
/usr/share/minetest/games/minimal/mods/default/textures/default_tnt_top.png
/usr/share/minetest/games/minimal/mods/default/textures/default_tool_mesepick.png
/usr/share/minetest/games/minimal/mods/default/textures/default_tool_steelaxe.png
/usr/share/minetest/games/minimal/mods/default/textures/default_tool_steelpick.png
/usr/share/minetest/games/minimal/mods/default/textures/default_tool_steelshovel.png
/usr/share/minetest/games/minimal/mods/default/textures/default_tool_steelsword.png
/usr/share/minetest/games/minimal/mods/default/textures/default_tool_stoneaxe.png
/usr/share/minetest/games/minimal/mods/default/textures/default_tool_stonepick.png
/usr/share/minetest/games/minimal/mods/default/textures/default_tool_stoneshovel.png
/usr/share/minetest/games/minimal/mods/default/textures/default_tool_stonesword.png
/usr/share/minetest/games/minimal/mods/default/textures/default_tool_woodaxe.png
/usr/share/minetest/games/minimal/mods/default/textures/default_tool_woodpick.png
/usr/share/minetest/games/minimal/mods/default/textures/default_tool_woodshovel.png
/usr/share/minetest/games/minimal/mods/default/textures/default_tool_woodsword.png
/usr/share/minetest/games/minimal/mods/default/textures/default_torch.png
/usr/share/minetest/games/minimal/mods/default/textures/default_torch_on_ceiling.png
/usr/share/minetest/games/minimal/mods/default/textures/default_torch_on_floor.png
/usr/share/minetest/games/minimal/mods/default/textures/default_tree.png
/usr/share/minetest/games/minimal/mods/default/textures/default_tree_top.png
/usr/share/minetest/games/minimal/mods/default/textures/default_water.png
/usr/share/minetest/games/minimal/mods/default/textures/default_wood.png
/usr/share/minetest/games/minimal/mods/default/textures/heart.png
/usr/share/minetest/games/minimal/mods/default/textures/player.png
/usr/share/minetest/games/minimal/mods/default/textures/player_back.png
/usr/share/minetest/games/minimal/mods/default/textures/treeprop.png
/usr/share/minetest/games/minimal/mods/default/textures/wieldhand.png
/usr/share/minetest/games/minimal/mods/errorhandler_test/init.lua
/usr/share/minetest/games/minimal/mods/experimental/depends.txt
/usr/share/minetest/games/minimal/mods/experimental/init.lua
/usr/share/minetest/games/minimal/mods/experimental/textures/experimental_dummyball.png
/usr/share/minetest/games/minimal/mods/experimental/textures/experimental_tester_tool_1.png
/usr/share/minetest/games/minimal/mods/give_initial_stuff/depends.txt
/usr/share/minetest/games/minimal/mods/give_initial_stuff/init.lua
/usr/share/minetest/games/minimal/mods/legacy/depends.txt
/usr/share/minetest/games/minimal/mods/legacy/init.lua
/usr/share/minetest/games/minimal/mods/legacy/textures/apple_iron.png
/usr/share/minetest/games/minimal/mods/legacy/textures/cooked_rat.png
/usr/share/minetest/games/minimal/mods/legacy/textures/dungeon_master.png
/usr/share/minetest/games/minimal/mods/legacy/textures/fireball.png
/usr/share/minetest/games/minimal/mods/legacy/textures/firefly.png
/usr/share/minetest/games/minimal/mods/legacy/textures/oerkki1.png
/usr/share/minetest/games/minimal/mods/legacy/textures/oerkki1_damaged.png
/usr/share/minetest/games/minimal/mods/legacy/textures/rat.png
/usr/share/minetest/games/minimal/mods/stairs/depends.txt
/usr/share/minetest/games/minimal/mods/stairs/init.lua
/usr/share/minetest/games/minimal/mods/test/init.lua
/usr/share/minetest/textures/base/pack/blank.png
/usr/share/minetest/textures/base/pack/camera_btn.png
/usr/share/minetest/textures/base/pack/chat_btn.png
/usr/share/minetest/textures/base/pack/debug_btn.png
/usr/share/minetest/textures/base/pack/down.png
/usr/share/minetest/textures/base/pack/down_arrow.png
/usr/share/minetest/textures/base/pack/drop_btn.png
/usr/share/minetest/textures/base/pack/fast_btn.png
/usr/share/minetest/textures/base/pack/fly_btn.png
/usr/share/minetest/textures/base/pack/gear_icon.png
/usr/share/minetest/textures/base/pack/halo.png
/usr/share/minetest/textures/base/pack/inventory_btn.png
/usr/share/minetest/textures/base/pack/jump_btn.png
/usr/share/minetest/textures/base/pack/left_arrow.png
/usr/share/minetest/textures/base/pack/logo.png
/usr/share/minetest/textures/base/pack/menu_bg.png
/usr/share/minetest/textures/base/pack/menu_header.png
/usr/share/minetest/textures/base/pack/minimap_mask_round.png
/usr/share/minetest/textures/base/pack/minimap_mask_square.png
/usr/share/minetest/textures/base/pack/minimap_overlay_round.png
/usr/share/minetest/textures/base/pack/minimap_overlay_square.png
/usr/share/minetest/textures/base/pack/no_screenshot.png
/usr/share/minetest/textures/base/pack/noclip_btn.png
/usr/share/minetest/textures/base/pack/object_marker_red.png
/usr/share/minetest/textures/base/pack/player_marker.png
/usr/share/minetest/textures/base/pack/rangeview_btn.png
/usr/share/minetest/textures/base/pack/rare_controls.png
/usr/share/minetest/textures/base/pack/right_arrow.png
/usr/share/minetest/textures/base/pack/server_flags_creative.png
/usr/share/minetest/textures/base/pack/server_flags_damage.png
/usr/share/minetest/textures/base/pack/server_flags_favorite.png
/usr/share/minetest/textures/base/pack/server_flags_pvp.png
/usr/share/minetest/textures/base/pack/smoke_puff.png
/usr/share/minetest/textures/base/pack/sunrisebg.png
/usr/share/minetest/textures/base/pack/unknown_item.png
/usr/share/minetest/textures/base/pack/unknown_node.png
/usr/share/minetest/textures/base/pack/unknown_object.png
/usr/share/minetest/textures/base/pack/up_arrow.png

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/minetest/*
%doc /usr/share/man/man6/*
