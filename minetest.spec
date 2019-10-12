#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : minetest
Version  : 5.1.0
Release  : 32
URL      : https://github.com/minetest/minetest/archive/5.1.0/minetest-5.1.0.tar.gz
Source0  : https://github.com/minetest/minetest/archive/5.1.0/minetest-5.1.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 CC-BY-SA-3.0 LGPL-2.1+ MIT
Requires: minetest-bin = %{version}-%{release}
Requires: minetest-data = %{version}-%{release}
Requires: minetest-license = %{version}-%{release}
Requires: minetest-man = %{version}-%{release}
BuildRequires : LuaJIT-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-mvn
BuildRequires : bzip2-dev
BuildRequires : curl-dev
BuildRequires : doxygen
BuildRequires : gmp-dev
BuildRequires : gradle
BuildRequires : irrlicht-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86misc-dev libXxf86vm-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libogg-dev
BuildRequires : libpng-dev
BuildRequires : libspatialindex-dev
BuildRequires : libvorbis-dev
BuildRequires : lua-dev
BuildRequires : mesa-dev
BuildRequires : ncurses-dev
BuildRequires : openal-soft-dev
BuildRequires : pkgconfig(libpng)
BuildRequires : pkgconfig(x11)
BuildRequires : postgresql-dev
BuildRequires : sqlite-autoconf-dev
BuildRequires : zlib-dev

%description
Minetest
========
[![Build Status](https://travis-ci.org/minetest/minetest.svg?branch=master)](https://travis-ci.org/minetest/minetest)
[![Translation status](https://hosted.weblate.org/widgets/minetest/-/svg-badge.svg)](https://hosted.weblate.org/engage/minetest/?utm_source=widget)
[![License](https://img.shields.io/badge/license-LGPLv2.1%2B-blue.svg)](https://www.gnu.org/licenses/old-licenses/lgpl-2.1.en.html)

%package bin
Summary: bin components for the minetest package.
Group: Binaries
Requires: minetest-data = %{version}-%{release}
Requires: minetest-license = %{version}-%{release}

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
Requires: minetest-man = %{version}-%{release}

%description doc
doc components for the minetest package.


%package extras
Summary: extras components for the minetest package.
Group: Default

%description extras
extras components for the minetest package.


%package license
Summary: license components for the minetest package.
Group: Default

%description license
license components for the minetest package.


%package man
Summary: man components for the minetest package.
Group: Default

%description man
man components for the minetest package.


%prep
%setup -q -n minetest-5.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1570900802
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake .. -DBUILD_CLIENT=1 \
-DBUILD_SERVER=1 \
-DENABLE_FREETYPE=1 \
-DBUILD_SHARED_LIBS=0
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1570900802
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/minetest
cp %{_builddir}/minetest-5.1.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/minetest/a91af6f95c72f679376baa29fba1fb2314589492
cp %{_builddir}/minetest-5.1.0/fonts/Arimo-LICENSE.txt %{buildroot}/usr/share/package-licenses/minetest/b1b13828a3a2be603b24a38d3948c7811d85f851
cp %{_builddir}/minetest-5.1.0/fonts/Cousine-LICENSE.txt %{buildroot}/usr/share/package-licenses/minetest/2b1b42e96714bc36f7bee9210a5e69e2586f7ee3
cp %{_builddir}/minetest-5.1.0/fonts/DroidSansFallbackFull-LICENSE.txt %{buildroot}/usr/share/package-licenses/minetest/2f6f017f448a7c197950c1d4a0907a9990845eb1
cp %{_builddir}/minetest-5.1.0/lib/lua/COPYRIGHT %{buildroot}/usr/share/package-licenses/minetest/a6efc4d11f332f4843bc25b557c6bf3e5ef51458
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/minetest

%files data
%defattr(-,root,root,-)
/usr/share/applications/net.minetest.minetest.desktop
/usr/share/icons/hicolor/128x128/apps/minetest.png
/usr/share/icons/hicolor/scalable/apps/minetest.svg
/usr/share/metainfo/net.minetest.minetest.appdata.xml
/usr/share/minetest/client/shaders/3d_interlaced_merge/opengl_fragment.glsl
/usr/share/minetest/client/shaders/3d_interlaced_merge/opengl_vertex.glsl
/usr/share/minetest/client/shaders/default_shader/opengl_fragment.glsl
/usr/share/minetest/client/shaders/default_shader/opengl_vertex.glsl
/usr/share/minetest/client/shaders/minimap_shader/opengl_fragment.glsl
/usr/share/minetest/client/shaders/minimap_shader/opengl_vertex.glsl
/usr/share/minetest/client/shaders/nodes_shader/opengl_fragment.glsl
/usr/share/minetest/client/shaders/nodes_shader/opengl_vertex.glsl
/usr/share/minetest/client/shaders/selection_shader/opengl_fragment.glsl
/usr/share/minetest/client/shaders/selection_shader/opengl_vertex.glsl
/usr/share/minetest/client/shaders/wielded_shader/opengl_fragment.glsl
/usr/share/minetest/client/shaders/wielded_shader/opengl_vertex.glsl
/usr/share/minetest/fonts/Arimo-LICENSE.txt
/usr/share/minetest/fonts/Arimo-Regular.ttf
/usr/share/minetest/fonts/Cousine-LICENSE.txt
/usr/share/minetest/fonts/Cousine-Regular.ttf
/usr/share/minetest/fonts/DroidSansFallbackFull-LICENSE.txt
/usr/share/minetest/fonts/DroidSansFallbackFull.ttf
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
/usr/share/minetest/games/minimal/mods/bucket/init.lua
/usr/share/minetest/games/minimal/mods/bucket/mod.conf
/usr/share/minetest/games/minimal/mods/bucket/textures/bucket.png
/usr/share/minetest/games/minimal/mods/bucket/textures/bucket_lava.png
/usr/share/minetest/games/minimal/mods/bucket/textures/bucket_water.png
/usr/share/minetest/games/minimal/mods/default/init.lua
/usr/share/minetest/games/minimal/mods/default/mapgen.lua
/usr/share/minetest/games/minimal/mods/default/mod.conf
/usr/share/minetest/games/minimal/mods/default/sounds/default_grass_footstep.1.ogg
/usr/share/minetest/games/minimal/mods/default/textures/bubble.png
/usr/share/minetest/games/minimal/mods/default/textures/crack_anylength.png
/usr/share/minetest/games/minimal/mods/default/textures/default_apple.png
/usr/share/minetest/games/minimal/mods/default/textures/default_book.png
/usr/share/minetest/games/minimal/mods/default/textures/default_bookshelf.png
/usr/share/minetest/games/minimal/mods/default/textures/default_brick.png
/usr/share/minetest/games/minimal/mods/default/textures/default_cactus_side.png
/usr/share/minetest/games/minimal/mods/default/textures/default_cactus_top.png
/usr/share/minetest/games/minimal/mods/default/textures/default_chest.png
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
/usr/share/minetest/games/minimal/mods/default/textures/default_river_water.png
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
/usr/share/minetest/games/minimal/mods/experimental/init.lua
/usr/share/minetest/games/minimal/mods/experimental/mod.conf
/usr/share/minetest/games/minimal/mods/experimental/modchannels.lua
/usr/share/minetest/games/minimal/mods/experimental/textures/experimental_dummyball.png
/usr/share/minetest/games/minimal/mods/experimental/textures/experimental_tester_tool_1.png
/usr/share/minetest/games/minimal/mods/experimental/textures/experimental_tiled.png
/usr/share/minetest/games/minimal/mods/give_initial_stuff/init.lua
/usr/share/minetest/games/minimal/mods/give_initial_stuff/mod.conf
/usr/share/minetest/games/minimal/mods/legacy/init.lua
/usr/share/minetest/games/minimal/mods/legacy/mod.conf
/usr/share/minetest/games/minimal/mods/legacy/textures/apple_iron.png
/usr/share/minetest/games/minimal/mods/legacy/textures/cooked_rat.png
/usr/share/minetest/games/minimal/mods/legacy/textures/dungeon_master.png
/usr/share/minetest/games/minimal/mods/legacy/textures/fireball.png
/usr/share/minetest/games/minimal/mods/legacy/textures/firefly.png
/usr/share/minetest/games/minimal/mods/legacy/textures/oerkki1.png
/usr/share/minetest/games/minimal/mods/legacy/textures/oerkki1_damaged.png
/usr/share/minetest/games/minimal/mods/legacy/textures/rat.png
/usr/share/minetest/games/minimal/mods/stairs/init.lua
/usr/share/minetest/games/minimal/mods/stairs/mod.conf
/usr/share/minetest/games/minimal/mods/test/crafting.lua
/usr/share/minetest/games/minimal/mods/test/formspec.lua
/usr/share/minetest/games/minimal/mods/test/init.lua
/usr/share/minetest/games/minimal/mods/test/mod.conf
/usr/share/minetest/games/minimal/mods/test/player.lua
/usr/share/minetest/locale/ca/LC_MESSAGES/minetest.mo
/usr/share/minetest/locale/cs/LC_MESSAGES/minetest.mo
/usr/share/minetest/locale/da/LC_MESSAGES/minetest.mo
/usr/share/minetest/locale/de/LC_MESSAGES/minetest.mo
/usr/share/minetest/locale/dv/LC_MESSAGES/minetest.mo
/usr/share/minetest/locale/el/LC_MESSAGES/minetest.mo
/usr/share/minetest/locale/eo/LC_MESSAGES/minetest.mo
/usr/share/minetest/locale/es/LC_MESSAGES/minetest.mo
/usr/share/minetest/locale/et/LC_MESSAGES/minetest.mo
/usr/share/minetest/locale/fil/LC_MESSAGES/minetest.mo
/usr/share/minetest/locale/fr/LC_MESSAGES/minetest.mo
/usr/share/minetest/locale/hu/LC_MESSAGES/minetest.mo
/usr/share/minetest/locale/id/LC_MESSAGES/minetest.mo
/usr/share/minetest/locale/it/LC_MESSAGES/minetest.mo
/usr/share/minetest/locale/ja/LC_MESSAGES/minetest.mo
/usr/share/minetest/locale/ja_KS/LC_MESSAGES/minetest.mo
/usr/share/minetest/locale/jbo/LC_MESSAGES/minetest.mo
/usr/share/minetest/locale/kk/LC_MESSAGES/minetest.mo
/usr/share/minetest/locale/kn/LC_MESSAGES/minetest.mo
/usr/share/minetest/locale/lo/LC_MESSAGES/minetest.mo
/usr/share/minetest/locale/lt/LC_MESSAGES/minetest.mo
/usr/share/minetest/locale/ms/LC_MESSAGES/minetest.mo
/usr/share/minetest/locale/my/LC_MESSAGES/minetest.mo
/usr/share/minetest/locale/nb/LC_MESSAGES/minetest.mo
/usr/share/minetest/locale/nl/LC_MESSAGES/minetest.mo
/usr/share/minetest/locale/nn/LC_MESSAGES/minetest.mo
/usr/share/minetest/locale/pl/LC_MESSAGES/minetest.mo
/usr/share/minetest/locale/pt/LC_MESSAGES/minetest.mo
/usr/share/minetest/locale/pt_BR/LC_MESSAGES/minetest.mo
/usr/share/minetest/locale/ro/LC_MESSAGES/minetest.mo
/usr/share/minetest/locale/ru/LC_MESSAGES/minetest.mo
/usr/share/minetest/locale/sl/LC_MESSAGES/minetest.mo
/usr/share/minetest/locale/sr_Cyrl/LC_MESSAGES/minetest.mo
/usr/share/minetest/locale/sv/LC_MESSAGES/minetest.mo
/usr/share/minetest/locale/sw/LC_MESSAGES/minetest.mo
/usr/share/minetest/locale/th/LC_MESSAGES/minetest.mo
/usr/share/minetest/locale/tr/LC_MESSAGES/minetest.mo
/usr/share/minetest/locale/uk/LC_MESSAGES/minetest.mo
/usr/share/minetest/locale/vi/LC_MESSAGES/minetest.mo
/usr/share/minetest/textures/base/pack/air.png
/usr/share/minetest/textures/base/pack/aux_btn.png
/usr/share/minetest/textures/base/pack/blank.png
/usr/share/minetest/textures/base/pack/camera_btn.png
/usr/share/minetest/textures/base/pack/chat_btn.png
/usr/share/minetest/textures/base/pack/chat_hide_btn.png
/usr/share/minetest/textures/base/pack/chat_show_btn.png
/usr/share/minetest/textures/base/pack/checkbox_16.png
/usr/share/minetest/textures/base/pack/checkbox_32.png
/usr/share/minetest/textures/base/pack/checkbox_64.png
/usr/share/minetest/textures/base/pack/debug_btn.png
/usr/share/minetest/textures/base/pack/down.png
/usr/share/minetest/textures/base/pack/drop_btn.png
/usr/share/minetest/textures/base/pack/error_screenshot.png
/usr/share/minetest/textures/base/pack/fast_btn.png
/usr/share/minetest/textures/base/pack/fly_btn.png
/usr/share/minetest/textures/base/pack/gear_icon.png
/usr/share/minetest/textures/base/pack/halo.png
/usr/share/minetest/textures/base/pack/ignore.png
/usr/share/minetest/textures/base/pack/inventory_btn.png
/usr/share/minetest/textures/base/pack/joystick_bg.png
/usr/share/minetest/textures/base/pack/joystick_center.png
/usr/share/minetest/textures/base/pack/joystick_off.png
/usr/share/minetest/textures/base/pack/jump_btn.png
/usr/share/minetest/textures/base/pack/loading_screenshot.png
/usr/share/minetest/textures/base/pack/logo.png
/usr/share/minetest/textures/base/pack/menu_bg.png
/usr/share/minetest/textures/base/pack/menu_header.png
/usr/share/minetest/textures/base/pack/minimap_btn.png
/usr/share/minetest/textures/base/pack/minimap_mask_round.png
/usr/share/minetest/textures/base/pack/minimap_mask_square.png
/usr/share/minetest/textures/base/pack/minimap_overlay_round.png
/usr/share/minetest/textures/base/pack/minimap_overlay_square.png
/usr/share/minetest/textures/base/pack/no_screenshot.png
/usr/share/minetest/textures/base/pack/noclip_btn.png
/usr/share/minetest/textures/base/pack/object_marker_red.png
/usr/share/minetest/textures/base/pack/player.png
/usr/share/minetest/textures/base/pack/player_back.png
/usr/share/minetest/textures/base/pack/player_marker.png
/usr/share/minetest/textures/base/pack/progress_bar.png
/usr/share/minetest/textures/base/pack/progress_bar_bg.png
/usr/share/minetest/textures/base/pack/rangeview_btn.png
/usr/share/minetest/textures/base/pack/rare_controls.png
/usr/share/minetest/textures/base/pack/refresh.png
/usr/share/minetest/textures/base/pack/server_flags_creative.png
/usr/share/minetest/textures/base/pack/server_flags_damage.png
/usr/share/minetest/textures/base/pack/server_flags_favorite.png
/usr/share/minetest/textures/base/pack/server_flags_pvp.png
/usr/share/minetest/textures/base/pack/server_ping_1.png
/usr/share/minetest/textures/base/pack/server_ping_2.png
/usr/share/minetest/textures/base/pack/server_ping_3.png
/usr/share/minetest/textures/base/pack/server_ping_4.png
/usr/share/minetest/textures/base/pack/smoke_puff.png
/usr/share/minetest/textures/base/pack/sunrisebg.png
/usr/share/minetest/textures/base/pack/unknown_item.png
/usr/share/minetest/textures/base/pack/unknown_node.png
/usr/share/minetest/textures/base/pack/unknown_object.png
/usr/share/minetest/textures/base/pack/zoom.png

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/minetest/*

%files extras
%defattr(-,root,root,-)
/usr/bin/minetestserver
/usr/share/minetest/builtin/async/init.lua
/usr/share/minetest/builtin/client/chatcommands.lua
/usr/share/minetest/builtin/client/death_formspec.lua
/usr/share/minetest/builtin/client/init.lua
/usr/share/minetest/builtin/client/register.lua
/usr/share/minetest/builtin/common/after.lua
/usr/share/minetest/builtin/common/async_event.lua
/usr/share/minetest/builtin/common/chatcommands.lua
/usr/share/minetest/builtin/common/filterlist.lua
/usr/share/minetest/builtin/common/information_formspecs.lua
/usr/share/minetest/builtin/common/misc_helpers.lua
/usr/share/minetest/builtin/common/serialize.lua
/usr/share/minetest/builtin/common/strict.lua
/usr/share/minetest/builtin/common/vector.lua
/usr/share/minetest/builtin/fstk/buttonbar.lua
/usr/share/minetest/builtin/fstk/dialog.lua
/usr/share/minetest/builtin/fstk/tabview.lua
/usr/share/minetest/builtin/fstk/ui.lua
/usr/share/minetest/builtin/game/auth.lua
/usr/share/minetest/builtin/game/chat.lua
/usr/share/minetest/builtin/game/constants.lua
/usr/share/minetest/builtin/game/deprecated.lua
/usr/share/minetest/builtin/game/detached_inventory.lua
/usr/share/minetest/builtin/game/falling.lua
/usr/share/minetest/builtin/game/features.lua
/usr/share/minetest/builtin/game/forceloading.lua
/usr/share/minetest/builtin/game/init.lua
/usr/share/minetest/builtin/game/item.lua
/usr/share/minetest/builtin/game/item_entity.lua
/usr/share/minetest/builtin/game/knockback.lua
/usr/share/minetest/builtin/game/misc.lua
/usr/share/minetest/builtin/game/privileges.lua
/usr/share/minetest/builtin/game/register.lua
/usr/share/minetest/builtin/game/statbars.lua
/usr/share/minetest/builtin/game/static_spawn.lua
/usr/share/minetest/builtin/game/voxelarea.lua
/usr/share/minetest/builtin/init.lua
/usr/share/minetest/builtin/mainmenu/common.lua
/usr/share/minetest/builtin/mainmenu/dlg_config_world.lua
/usr/share/minetest/builtin/mainmenu/dlg_contentstore.lua
/usr/share/minetest/builtin/mainmenu/dlg_create_world.lua
/usr/share/minetest/builtin/mainmenu/dlg_delete_content.lua
/usr/share/minetest/builtin/mainmenu/dlg_delete_world.lua
/usr/share/minetest/builtin/mainmenu/dlg_rename_modpack.lua
/usr/share/minetest/builtin/mainmenu/dlg_settings_advanced.lua
/usr/share/minetest/builtin/mainmenu/generate_from_settingtypes.lua
/usr/share/minetest/builtin/mainmenu/init.lua
/usr/share/minetest/builtin/mainmenu/pkgmgr.lua
/usr/share/minetest/builtin/mainmenu/tab_content.lua
/usr/share/minetest/builtin/mainmenu/tab_credits.lua
/usr/share/minetest/builtin/mainmenu/tab_local.lua
/usr/share/minetest/builtin/mainmenu/tab_online.lua
/usr/share/minetest/builtin/mainmenu/tab_settings.lua
/usr/share/minetest/builtin/mainmenu/tab_simple_main.lua
/usr/share/minetest/builtin/mainmenu/textures.lua
/usr/share/minetest/builtin/profiler/init.lua
/usr/share/minetest/builtin/profiler/instrumentation.lua
/usr/share/minetest/builtin/profiler/reporter.lua
/usr/share/minetest/builtin/profiler/sampling.lua
/usr/share/minetest/builtin/settingtypes.txt

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/minetest/2b1b42e96714bc36f7bee9210a5e69e2586f7ee3
/usr/share/package-licenses/minetest/2f6f017f448a7c197950c1d4a0907a9990845eb1
/usr/share/package-licenses/minetest/a6efc4d11f332f4843bc25b557c6bf3e5ef51458
/usr/share/package-licenses/minetest/a91af6f95c72f679376baa29fba1fb2314589492
/usr/share/package-licenses/minetest/b1b13828a3a2be603b24a38d3948c7811d85f851

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man6/minetest.6
/usr/share/man/man6/minetestserver.6
